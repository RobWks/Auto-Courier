#Inputs: Graph, Start node, End node

import numpy as np
import math
import scipy.sparse.csgraph as csg
from scipy.sparse import csr_matrix

graph = np.load('graph.npy')
nodes = np.reshape(graph,(len(graph)*2,2))
nodes = np.unique([tuple(row) for row in nodes])
count = 0.0;

n = len(nodes)
csgraph_dense = np.zeros((n,n))
csgraph_dense[:] = float('inf')
for point in graph:
	p1 = np.where(np.all(nodes==point[0],axis=1))
	p2 = np.where(np.all(nodes==point[1],axis=1))
	csgraph_dense[p1,p2] = math.sqrt((point[1][1]-point[0][1])**2+(point[1][0]-point[0][0])**2)
	csgraph_dense[p2,p1] = csgraph_dense[p1,p2]

csgraph_dense = np.ma.masked_values(csgraph_dense, 0)
csgraph_sparse = csr_matrix(csgraph_dense)

dist_matrix,predecessors = csg.shortest_path(csgraph_sparse,return_predecessors=True)

start = int(raw_input('Start? '))
dest = int(raw_input('Destination? '))

distance = dist_matrix[start,dest]
path = []
pred = dest

while pred!=start:
	pred = predecessors[start,pred]
	path.append(pred)


path.reverse()
path.append(dest)

print path
print distance


