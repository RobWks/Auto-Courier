import numpy as np

graph = np.load('graph.npy')
nodes = np.reshape(graph,(len(graph)*2,2))
nodes = np.unique([tuple(row) for row in nodes])
count = 0.0;

n = len(nodes)
csgraph = np.zeros((n,n))
for i in range(n):
	test_node = nodes[i]
	for j in range(len(graph)):
		count = count +1.0
		print count/(n*len(graph))*100
		if np.array_equal(test_node,graph[j][0]):
			match = np.where(np.all(nodes==graph[j][1],axis=1))
			csgraph[i,match] = True
			csgraph[match,i] = True


