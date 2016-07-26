#!/usr/bin/env python

""""
Circle Motion
Simple publisher script to drive the turtlebot in circles
"""

__author__ = "Robert Weeks"
__version__ = "1.0"
__email__ = "rweeks@uwaterloo.ca"

import rospy
from geometry_msgs.msg import Twist
import numpy as np
from geometry_msgs.msg import PoseStamped
import math
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from actionlib_msgs.msg import *
#from geometry_msgs.msg import PoseWithCovarianceStamped
#from tf.transformations import euler_from_quaternion
#317 pixels = 12m

def talker():
	rospy.init_node('CircleMotion', anonymous=True)

	file_loc = '/home/rob/Auto-Courier/Maps/E5/Directory/e5.csv'
	csv_file = np.genfromtxt(file_loc,delimiter=',',dtype=None)
	img_height = 768;
	img_width = 2250;

	directory = {}
	for i in csv_file:
		x = i[1]*12.0/317
		y = (img_height-i[2])*12.0/317
		if i[3] == 'u':
			direction = math.pi/2 
		elif i[3] == 'r':
			direction = 0 
		elif i[3] == 'l':
			direction = math.pi/2 
		else:
			direction = 3*math.pi/2 

		directory[str(i[0])] = [x,y,direction]

	pickup=raw_input('Where should I pick up the package? (Room #): ')
	dest = raw_input('Where should I deliver the package? (Room #): ')

	room1 = 'I need to go from room {} with location ({},{},{})'.format(pickup,*directory[pickup])
	room2 = 'to room {} with location ({},{},{}).'.format(dest,*directory[dest])
	print room1 + room2

	# (roll,pitch,yaw) = euler_from_quaternion(quaternion)
	#Initialize
	client = actionlib.SimpleActionClient('Move_base', MoveBaseAction)

	client.wait_for_server(rospy.Duration(5))

	#Create publisher used to send out twist
	goal = MoveBaseGoal()

	#Set update rate to 20 Hz
	rate = rospy.Rate(20) 

	goal.target_pose.header.frame_id = "map"
	goal.target_pose.header.stamp = rospy.Time.now()
	goal.target_pose.pose.position.z = 0.0
	goal.target_pose.pose.position.x = directory[dest][0]
	goal.target_pose.pose.position.y = directory[dest][1]
	goal.target_pose.pose.orientation.z = math.sin(directory[dest][2]/2)
	goal.target_pose.pose.orientation.w = math.cos(directory[dest][2]/2)

	client.send_goal(goal)

	client.wait_for_result()

	# Allow TurtleBot up to 60 seconds to complete task
	success = client.wait_for_result(rospy.Duration(60)) 

        state = client.get_state()
        result = False

        if success and state == GoalStatus.SUCCEEDED:
            # We made it!
            result = True
        else:
            moveclient.cancel_goal()

        client.goal_sent = False

        rospy.loginfo(str(result))


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
	