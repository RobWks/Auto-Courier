#!/usr/bin/env python

""""
CircleMotion
Simple publisher script to drive the turtlebot in circles
"""

__author__ = "Robert Weeks"
__version__ = "1.0"
__email__ = "rweeks@uwaterloo.ca"

import rospy
from geometry_msgs.msg import Twist
from geometry_msgs.msg import PoseWithCovarianceStamped
from tf.transformations import euler_from_quaternion

def callback(data):
	X = msg.pose.pose.position.x #Robot X psotition
	Y = msg.pose.pose.position.y #Robot Y psotition
	(roll,pitch,yaw) = euler_from_quaternion(msg.pose.pose.orientation)
	rospy.loginfo("pose_callback X: {}} Y: {} Yaw: {}".format(X, Y, yaw))

#def listener():


def main():
	# (roll,pitch,yaw) = euler_from_quaternion(quaternion)
	#Initialize
	rospy.init_node('CircleMotion', anonymous=True)

	#Create publisher used to send out twist
	pub = rospy.Publisher('/cmd_vel_mux/input/navi', Twist, queue_size=10)
	rospy.Subscriber("/amcl_pose", Twist, callback)


	#Set update rate to 20 Hz
	rate = rospy.Rate(20) 

	#while script hasn't been canceled (ctrl + c)
	while not rospy.is_shutdown():
		# Twist is a datatype for velocity
		move_cmd = Twist()
		# let's go forward at 0.2 m/s
		move_cmd.linear.x = 0.1
		# let's turn at 0.2 radians/s
		move_cmd.angular.z = 0.2
		#publish twist
		pub.publish(move_cmd)
		#Sleep for 0.05 seconds
		rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
	