import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d
from scipy.spatial import Delaunay


e5_map = np.genfromtxt('e5_smaller.csv',delimiter=',')
e5_map = np.reshape(e5_map/100,[384,1125])
e5_map = e5_map.astype(bool)
[M,N]= e5_map.shape
#print e5_map.shape
plt.imshow(e5_map)
#plt.show()

num_obstacles = 5000;
x_o = np.round(np.random.rand(1,num_obstacles)*(N-1))
y_o = np.round(np.random.rand(1,num_obstacles)*(M-1))


ind_delete = []
for i in range(len(x_o[0])):
    if e5_map[y_o[0][i]][x_o[0][i]]:
        ind_delete.append(i)

x_o = np.delete(x_o,ind_delete)
y_o = np.delete(y_o,ind_delete)
plt.plot(x_o,y_o,'g*')

x_o = x_o.reshape(len(x_o),1)
y_o = y_o.reshape(len(y_o),1)

points = np.concatenate((x_o,y_o),axis=1)

tri = Delaunay(points)
plt.triplot(points[:,0], points[:,1], tri.simplices.copy())
plt.plot(points[:,0], points[:,1], 'o')
plt.show()