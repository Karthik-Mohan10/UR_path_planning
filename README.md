# UR path planning

This is a package for ARTag guided path planning of a Universal Robot using ROS.

The objective of the task is to execute a 2D welding path by the UR3e robot.

The task includes;
1. Use the usb_cam library package to publish the video output from a fixed USB camera attached to the robot environment
2. Utilize the ar_track_alvar package for pose estimation of the desired welding points using ARTags
3. Addition of obstacles around the physical robot to the scene for collision checking
4. Crete an action server node that accepts the ARTag poses as inputs and executes robot motion using Moveit framework

An example of welding path
<p align="center">
  <img src="Welding path" width="350" title="hover text" alt="accessibility text" >
</p>