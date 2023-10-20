from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

collab_graph = np.loadtxt(
    "ca-GrQc.txt", dtype=int, comments="#", usecols=(0, 1)
)


graph = [[0, 1, 2, 0], [0, 0, 0, 1], [0, 0, 0, 3], [0, 0, 0, 0]]
graph = csr_matrix(graph)
G = nx.Graph(graph)
nx.draw(G, with_labels=True)
plt.show()
# print(G)

dist_matrix, predecessors = dijkstra(
    csgraph=graph, directed=False, indices=0, return_predecessors=True
)
dist_matrix
