# UR path planning

This is a package for ARTag guided path planning of a Universal Robot using ROS.

The objective of the task is to execute a 2D welding path by the UR3e robot.

The task includes;
1. Use the *usb_cam* library package to publish the video output from a fixed USB camera attached to the robot environment(*webcam_launch.launch*)
2. Utilize the *ar_track_alvar* package for pose estimation of the desired welding points using ARTags (*artag_track.launch*)
3. Addition of obstacles around the physical robot to the scene for collision checking - Ground plane, camera system and other physical structures are added along with the welding nozzle to the planning scene (*configure_robot_env.py* & *safety_feature.launch*)
4. Crete an action server node that accepts the ARTag poses as inputs and executes robot motion using Moveit framework (*robot_mover_action_server.py*)
5. Finally, run the *safety_feature* launch file to launch robot along with camera, ARTag and all transforms, run *robot_mover_action_server.py* to start the action server, and then run *welding_path_teaching.py* to start the client and to send the pose array of welding points captured manually

**Example of a welding path**

![alt text](https://github.com/Karthik-Mohan10/UR_path_planning/blob/main/Welding%20path.JPG?raw=true)

**ARTags**

![alt text](https://github.com/Karthik-Mohan10/UR_path_planning/blob/main/ARTags.JPG?raw=true)