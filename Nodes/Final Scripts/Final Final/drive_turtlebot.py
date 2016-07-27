import numpy as np
import matplotlib.pyplot as plt
import math

def main():
	#Import and clean up the data
	nodes = np.load('nodes.npy')
	path = np.load('path.npy')
	path = np.array([l[0] for l in path.tolist()])
	path = path.reshape(1,len(path))

	coords = nodes[path][0]
	map_res = 0.07570977917981073
	coords = coords*map_res
	print coords
	print len(coords)
	way_move_cmd = waypoints_to_commands(coords)

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

def waypoints_to_commands(coords):
	#cmd = [[vx,az,time],etc]
	#Convert waypoints to value in stage
	lin_vel = 0.2
	ang_vel = math.radians(45)    #45 deg/s in rad/s
	init_ang = 0;
	move_ang = [0]
	move_dist = [0]
	for i in range(len(coords)-1):
		p1 = coords[i]
		p2 = coords[i+1]
		move_ang.append(math.atan2(p2[1]-p1[1],p2[0]-p1[0]))
		move_dist.append(math.sqrt((p2[1]-p1[1])**2+(p2[0]-p1[0])**2))

	print np.degrees(move_ang)
	print len(move_dist)
	move_cmd = []

	for i in range(len(move_ang)-1):
		ang_cmd = (move_ang[i+1]-move_ang[i])
		ang_time = ang_cmd/ang_vel
		dist_cmd =move_dist[i+1]-move_dist[i]
		dist_time = dist_cmd/lin_vel
		move_cmd.append([0,np.sign(ang_cmd),math.fabs(ang_time)])
		move_cmd.append([np.sign(dist_cmd),0,math.fabs(dist_time)])

	print move_cmd
	print len(move_cmd)
	return move_cmd

	

if __name__ == '__main__':
    main()