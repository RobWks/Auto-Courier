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
#from geometry_msgs.msg import PoseWithCovarianceStamped
#from tf.transformations import euler_from_quaternion

def talker():
	# (roll,pitch,yaw) = euler_from_quaternion(quaternion)
	#Initialize
	rospy.init_node('CircleMotion', anonymous=True)

	#Create publisher used to send out twist
	pub = rospy.Publisher('cmd_vel_mux/input/navi', Twist, queue_size=10)

	#Set update rate to 20 Hz
	rate = rospy.Rate(10) 

	# Twist is a datatype for velocity
	move_cmd = Twist()
	# let's go forward at 0.2 m/s
	move_cmd.linear.x = 0.2
	# let's turn at 0.2 radians/s
	move_cmd.angular.z = 0.2
	
	#while script hasn't been canceled (ctrl + c)
	while not rospy.is_shutdown():
		#publish twist
		pub.publish(move_cmd)
		#Sleep for 0.05 seconds
		rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
	