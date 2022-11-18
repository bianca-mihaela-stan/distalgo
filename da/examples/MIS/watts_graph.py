
#%%
from asyncore import write
import networkx as nx

G = nx.connected_watts_strogatz_graph(100, 4, 0.8, 10);

nx.draw(G, node_size = 30)
A = nx.adjacency_data(G)['adjacency']
print(A)

f = open("graph3.txt", "w")
for i in range(0, 100):
    f.write(f"{i + 1} : ")
    for neigh in A[i]:
        if neigh != i:
            f.write(f"{neigh['id'] + 1} ");
    f.write("\n")

# %%
