import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d

e5_map = np.genfromtxt('e5_smaller.csv',delimiter=',')
e5_map = np.reshape(e5_map/100,[384,1125])
e5_map = e5_map.astype(bool)
[M,N]= e5_map.shape
#print e5_map.shape
plt.imshow(e5_map)
plt.show()



