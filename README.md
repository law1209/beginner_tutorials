This is the beginner_tutorial for ROS Noetic
Ubuntu 20.04

Please copy this file to ~/catkin_ws/src/beginner_tutorial

Then run the following commands in the terminal
Then folowing the scripts in the tutorial

cd ~/catkin_ws
catkin_make
source devel/setup.bash
roscore

rosrun beginner_tutorial add_two_ints_server.py
rosrun beginner_tutorial add_two_ints_client.py 2 3



