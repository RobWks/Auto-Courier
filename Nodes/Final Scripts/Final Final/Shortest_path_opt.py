#Inputs: Graph, Start node, End node
#Outputs: Coordinate from start to finish

import numpy as np
import math
import scipy.sparse.csgraph as csg
from scipy.sparse import csr_matrix

start_point = np.array([26.416666666666668,26.416666666666668])
end_point = np.array([503,288])

graph = np.load('graph.npy')
nodes = np.reshape(graph,(len(graph)*2,2))

"""
#Old code to calculate unique rows, has some sort of bug?
nodes = np.unique([tuple(row) for row in nodes])
"""

#Code to calculate unique nodes
b = np.ascontiguousarray(nodes).view(np.dtype((np.void, nodes.dtype.itemsize * nodes.shape[1])))
_, idx = np.unique(b, return_index=True)
nodes = nodes[idx]

end_node = np.where(np.all(nodes==end_point,axis=1))
start_node = np.where(np.all(nodes==start_point,axis=1))

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

print end_node
print start_node

distance = dist_matrix[start_node,end_node]
print distance.tolist()

path = []
pred = end_node

while pred!=start_node:
	pred = predecessors[start_node,pred]
	path.append(pred.tolist())


path.reverse()
path.append(end_node)
np.save('path.npy',path)
np.save('nodes.npy',nodes)

print path



