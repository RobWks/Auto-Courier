#!/usr/bin/env python

""""
Calculate Graph
Script to generate path planning graph.

Input is 
"""

__author__ = "Robert Weeks"
__version__ = "1.0"
__email__ = "rweeks@uwaterloo.ca"

import rospy
from std_msgs.msg import String
from nav_msgs.msg import OccupancyGrid
import numpy as np
import matplotlib.pyplot as plt

def map_callback(data):
    e5_map = data.data
    np.savetxt('e5_smaller.csv', e5_map, delimiter=',')
    plt.imsave('map_test.png', e5_map)
    
def listener():

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("/map", OccupancyGrid, map_callback)

    rospy.spin()

if __name__ == '__main__':
    listener()
