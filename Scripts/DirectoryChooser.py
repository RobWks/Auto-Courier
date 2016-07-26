__Author__ = "Robert Weeks"
__Email__ = "rweeks@uwaterloo.ca"

#Script to choose delivery location

import numpy as np

file_loc = '/home/rob/Auto-Courier/Maps/E5/Directory/e5.csv'
csv_file = np.genfromtxt(file_loc,delimiter=',',dtype=None)

directory = {}
for i in csv_file:
	directory[str(i[0])] = [i[1],i[2],i[3]]

pickup=raw_input('Where should I pick up the package? (Room #): ')
dest = raw_input('Where should I deliver the package? (Room #): ')

room1 = 'I need to go from room {} with location ({}.{},{})'.format(pickup,*directory[pickup])
room2 = 'to room {} with location ({}.{},{}).'.format(dest,*directory[dest])
print room1 + room2

38.0820189274,7.26813880126

rostopic pub /move_base_simple/goal geometry_msgs/PoseStamped '{header: {stamp: now, frame_id: "map"}, pose: {position: {x: 48.0, y: 8.0, z: 0.0}, orientation: {w: 1.0}}}'

rostopic pub /move_base_simple/goal geometry_msgs/PoseStamped '{header: {stamp: now, frame_id: "map"}, pose: {position: {x: 12.0, y: 2.0, z: 0.0}, orientation: {w: 1.0}}}'