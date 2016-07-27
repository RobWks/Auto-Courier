#!/usr/bin/env python

import rospy
import numpy as np
import matplotlib.pyplot as plt
from geometry_msgs.msg import Twist
import math
import time

class DrawASquare():
	def __init__(self):
		# initiliaze
		rospy.init_node('drawasquare', anonymous=False)
		# What to do you ctrl + c    
		rospy.on_shutdown(self.shutdown)
		self.cmd_vel = rospy.Publisher('cmd_vel_mux/input/navi', Twist, queue_size=10)
		self.main()

	def main(self):
		rospy.loginfo("Turning")
    	#Import and clean up the data
		nodes = np.load('nodes.npy')
		path = np.load('path.npy')
		path = np.array([l[0] for l in path.tolist()])
		path = path.reshape(1,len(path))
		coords = nodes[path][0]

		rospy.loginfo("done loading")

		move_cmd = Twist()
		move_cmd.linear.x = 0.2

		rospy.loginfo("done loading 2")

		turn_cmd = Twist()
		turn_cmd.linear.x = 0
		turn_cmd.angular.z = math.radians(45)

		rospy.loginfo("Calc waypoints")
		way_move_cmd = self.waypoints(coords)

		rospy.loginfo("Calc waypoints2")

		r = rospy.Rate(5)

		for move in way_move_cmd:
			rospy.loginfo("Calc waypoints2.5")
			if move[0] == 0:
				timeout1 = time.time() + move[2]+0.1
				while True:
					#Ang motion
					rospy.loginfo("Turning")
					turn_cmd.angular.z = move[1]*math.radians(45)
					rospy.loginfo(turn_cmd)
					self.cmd_vel.publish(turn_cmd)
					if time.time() > timeout1:
						break
					r.sleep()
			else:
				timeout2 = time.time() + move[2]+0.1
				while True:
					#linear motion
					rospy.loginfo("Driving")
					self.cmd_vel.publish(move_cmd)
					rospy.loginfo(move_cmd)
					if time.time() > timeout2:
						break
					r.sleep()

		rospy.loginfo("Calc waypoints3")
		"""
		#Plotting fun
		e5_map = np.genfromtxt('e5_smaller.csv',delimiter=',')
		e5_map = np.reshape(e5_map/100,[384,1125])
		e5_map = e5_map.astype(bool)
		[M,N]= e5_map.shape
		plt.imshow(e5_map)
		plt.hold(True)
		plt.plot(coords[:,0],coords[:,1],'r')
		plt.axis('equal')
		plt.axis([0,1125,0,384])
		plt.show()
		"""

	def waypoints(self,coords):
		#cmd = [[vx,az,time],etc]
		#Convert waypoints to value in stage
		rospy.loginfo("in waypoints")
		lin_vel = 0.2
		ang_vel = math.radians(45)    #45 deg/s in rad/s
		map_res = 0.07570977917981073
		init_ang = 0;
		coords = coords*map_res
		move_ang = [0]
		move_dist = []

		rospy.loginfo("in waypoints1")
		for i in range(len(coords)-1):
			p1 = coords[i]
			p2 = coords[i+1]
			#move_ang.append(math.atan2(p2[1]-p1[1],p2[0]-p1[0]))
			move_ang.append(math.atan2(p2[1]-p1[1],p2[0]-p1[0]))
			move_dist.append(math.sqrt((p2[1]-p1[1])**2+(p2[0]-p1[0])**2))

		lin_move_cmd = []

		rospy.loginfo("in waypoints2")
		for i in range(len(move_ang)-1):
			ang_cmd = (move_ang[i+1]-move_ang[i])
			ang_time = ang_cmd/ang_vel
			dist_cmd =move_dist[i]
			dist_time = dist_cmd/lin_vel
			lin_move_cmd.append([0,np.sign(ang_cmd),math.fabs(ang_time)])
			lin_move_cmd.append([1.0,0,math.fabs(dist_time)])

		rospy.loginfo("leaving waypoints")
		return lin_move_cmd

	#Create required moves
	def shutdown(self):
		# stop turtlebot
		rospy.loginfo("Stop Drawing Squares")
		self.cmd_vel.publish(Twist())
		rospy.sleep(1)

if __name__ == '__main__':
    try:
        DrawASquare()
    except:
        rospy.loginfo("node terminated.")