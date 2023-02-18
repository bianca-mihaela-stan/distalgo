
#%%
from asyncore import write
import networkx as nx
import random

n = 5

for y in range (0, 1):
    G = nx.connected_watts_strogatz_graph(n, 4, 0.8, 10)
    
    weights = list(range(1,(n*10)))
    nodes_to_weights = [[None for x in range(0,n)] for x in range(0,n)]

    nx.nx_agraph.to_agraph(G)
    A = nx.adjacency_data(G)['adjacency']

    f = open(f"../graphs/{n}/graph{y}.txt", "w")
    
    # print(nodes_to_weights)
    
    for i in range(0,n):
        for j in range(0,n):
            # print(i,j, nodes_to_weights[i][j])
            if nodes_to_weights[i][j] == None:
                weight = random.choice(weights)
                # print(weight)
                nodes_to_weights[i][j] = weight
                nodes_to_weights[j][i] = weight
                weights.remove(weight)
    
    # print(nodes_to_weights)

    for i in range(0, n):
        f.write(f"{i + 1} : ")
        for neigh in A[i]:
            if neigh != i:
                id = neigh['id']
                print(i, id, nodes_to_weights[i][id])
                f.write(f"{neigh['id'] + 1},")
                f.write(f"{nodes_to_weights[i][id]} ")
        f.write("\n")

# %%
