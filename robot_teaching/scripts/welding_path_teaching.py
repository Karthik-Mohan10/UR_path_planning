#!/usr/bin/env python3

import rospy
from tf2_ros import Buffer, TransformListener, TransformBroadcaster
import tf_conversions
from ar_track_alvar_msgs.msg import AlvarMarker, AlvarMarkers
import actionlib
import math

import tf2_ros
import tf2_geometry_msgs
from geometry_msgs.msg import Pose, Point, Quaternion, PoseStamped, TransformStamped


from welding_robot_msgs.msg import WeldingPathAction 
from welding_robot_msgs.msg import WeldingPathActionFeedback
from welding_robot_msgs.msg import WeldingPathActionGoal
from welding_robot_msgs.msg import WeldingPathActionResult
from welding_robot_msgs.msg import WeldingPathFeedback
from welding_robot_msgs.msg import WeldingPathGoal
from welding_robot_msgs.msg import WeldingPathResult

tfbuffer = None
listener = None

pose = None	
pose_list = []

client = actionlib.SimpleActionClient("robot_mover_action_server", WeldingPathAction)

def ar_tag_estimate_callback(msg):
    """Callback from topic subscriber."""
    
    global pose
    
    markers = msg.markers
   
    try:
        pose = msg.markers[0].pose

    except:
        print("AR not found")
        

def main():

    global pose_list, pose, tfbuffer, listener
    tfbuffer = tf2_ros.Buffer(rospy.Duration(2.0))
    listener = tf2_ros.TransformListener(tfbuffer)
    tfbroadcast = tf2_ros.TransformBroadcaster()
  

    while True:

        #tfbroadcast.sendTransform(nozzle_transform)
        n = input("press e to exit & s to save pos : ")
        if n == 's':
        

            print("base coordinates----")
            print(pose)
            #t = tfbuffer.lookup_transform("base_link", "ar_marker_13a", rospy.Time(0), rospy.Duration(0.5))
            t = tfbuffer.lookup_transform("base_link", "tcp_goal", rospy.Time(0), rospy.Duration(0.5))

            pose = PoseStamped()
            pose.header = t.header
            pose.pose.orientation = t.transform.rotation
            pose.pose.position = t.transform.translation  
            #Offset in z direction to maintain necessary gap with the ground
            pose.pose.position.z += .03
            #pose.pose.orientation.x = 0
            #pose.pose.orientation.y = 0

            print("Transformed pose-------")
            print(pose)
            
            pose_list.append(pose)
    
        elif n == 'e':
            print(pose_list)
            break
            
def test_client():
    client = actionlib.SimpleActionClient("robot_mover_action_server", WeldingPathAction)
    rospy.loginfo("waiting for server...")
    client.wait_for_server()
    
    goal = WeldingPathGoal(poses=pose_list)
    client.send_goal(goal)
    
    rospy.loginfo("Goal sent, waiting for result...")
    client.wait_for_result()
    result = client.get_result()
    
    if result is not None:
        rospy.loginfo("Result Received")
    else:
        rospy.loginfo("Result not received")
   
    
    
if __name__ == "__main__":
    rospy.init_node("teaching_transform_node")

    rospy.Subscriber("/ar_pose_marker", AlvarMarkers, ar_tag_estimate_callback)
    main()
    test_client()
    
    

