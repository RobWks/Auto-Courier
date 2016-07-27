import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d
from scipy.spatial import distance
import random
import math
import time

def main():
    e5_map = np.genfromtxt('e5_smaller.csv',delimiter=',')
    e5_map = np.reshape(e5_map/100,[384,1125])
    e5_map = e5_map.astype(bool)
    [M,N]= e5_map.shape

    plt.imshow(e5_map)

    num_obstacles = 2000;
    x_o = np.round(np.random.rand(1,num_obstacles)*(N-1))
    y_o = np.round(np.random.rand(1,num_obstacles)*(M-1))


    ind_delete = []
    for i in range(len(x_o[0])):
        if e5_map[y_o[0][i]][x_o[0][i]]:
            ind_delete.append(i)

    x_o = np.delete(x_o,ind_delete)
    y_o = np.delete(y_o,ind_delete)


    x_o = x_o.reshape(len(x_o),1)
    y_o = y_o.reshape(len(y_o),1)

    points = np.concatenate((x_o,y_o),axis=1)
    print points.shape
    print '1'

    dist_from_points = np.zeros((len(points),len(points)))
    count = 0.0;

    for i in range(len(points)):
        for j in range(len(points)):
            count = count +1.0
            print 'Loading %{:3.1f}'.format((count/len(points)**2)*100.0)
            #dist_from_points[i][j] = distance.euclidean(points[i],points[j])
            dist_from_points[i][j] = (points[i][1]-points[j][1])**2+(points[i][0]-points[j][0])**2



    numb_close = 30; #Number of closest points that you want to connect
    neighbors = np.zeros((numb_close+1,len(dist_from_points)))
    index_tool = range(len(dist_from_points))

    print '1.5'

    for i in range(numb_close+1): #1 is added due to closest being itself
        neighbors[i] = np.argmin(dist_from_points, axis = 1)
        neighbors = neighbors.astype(int)
        dist_from_points[index_tool,neighbors[i]] = float('inf')

    print '2'
    neighbors = np.delete(neighbors,0,axis=0)
    matches = []

    for i in range(len(neighbors[0])):
        for j in range(len(neighbors)):
            matches.append([points[i],points[neighbors[j][i]]])
    
    print '3'

    count = 0;
    for pair in matches:
        if not check_line_collision(pair,0.4,e5_map):
            plt.plot([pair[0][0],pair[1][0]],[pair[0][1],pair[1][1]],'g')
        #else:
            #plt.plot([pair[0][0],pair[1][0]],[pair[0][1],pair[1][1]],'r')

    print 'End' 

    plt.axis('equal')
    plt.axis([0,1125,0,384])
    plt.show()

def check_line_collision(point_pair,dx,locmap):
    for q in [-6,6]:
        for r in [-6,6]:
            p1 = point_pair[0]+q
            p2 = point_pair[1]+r
            theta = math.atan2(p2[1]-p1[1],p2[0]-p1[0])
            i_comp = dx*math.cos(theta)
            j_comp = dx*math.sin(theta)

            if i_comp == 0.0:
                num_steps = range(int(round((p2[1]-p1[1])/j_comp+1)))
            else:    
                num_steps = range(int(round((p2[0]-p1[0])/i_comp+1)))

            disc_points = np.zeros((len(num_steps),2))

            for i in num_steps:
                disc_points[i,0] = p1[0] + i_comp*i
                disc_points[i,1] = p1[1] + j_comp*i
                if locmap[round(disc_points[i,1])][round(disc_points[i,0])]:
                    return True
        
    return False

if __name__ == '__main__':
    main()


#point_pair = [[10,16],[32,8]]
#dx = 0.1
