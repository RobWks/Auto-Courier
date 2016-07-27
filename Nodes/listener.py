#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from nav_msgs.msg import OccupancyGrid
import numpy as np
import matplotlib.pyplot as plt

def map_callback(data):
    e5_map = data.data
    #np.savetxt('test.csv', e5_map, delimiter=',')
    e5_map = np.array(e5_map) 
    e5_map = np.reshape(e5_map/100,[384,1125])
    e5_map = e5_map.astype(bool)
    [M,N]= e5_map.shape
    plt.imsave('map_test.png', e5_map)

    #plt.imshow(e5_map)
    #plt.axis('equal')
    #plt.axis([0,384,0,1125])
    #plt.show
    
    """
    num_obstacles = 5000;
    x_o = np.round(np.random.rand(1,num_obstacles)*(N-1))+1
    y_o = np.round(np.random.rand(1,num_obstacles)*(M-1))+1


    ind_delete = []
    for i in range(len(x_o[0]))[::-1]:
        if e5_map[y_o[0][i]][x_o[0][i]]:
            ind_delete.append(i)

    x_o = np.delete(x_o,ind_delete)
    y_o = np.delete(y_o,ind_delete)
    plt.plot(x_o,y_o,'*')
    plt.axis('equal')
    plt.axis([0,384,0,1125])
    plt.show()
    """
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("/map", OccupancyGrid, map_callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
