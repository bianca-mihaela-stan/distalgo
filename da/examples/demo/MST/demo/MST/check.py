import sys
import networkx as nx

nr_nodes = int(sys.argv[1])
nr_neighbors = int(sys.argv[2])
which_graph = int(sys.argv[3])
which_run = int(sys.argv[4])

file = f"/home/bianca/licenta/distalgo/da/examples/demo/MST/results/{which_run}/node_results.txt"
f = open(file)
graph = f"/home/bianca/licenta/distalgo/da/examples/MST/graphs/{nr_nodes}/neighbors_{nr_neighbors}/graph{which_graph}.txt"
f2 = open(graph)

def convert(s):
    return list(map(lambda x: x, s))

correct = True

# Create the NetworkX graph.
G = nx.Graph()
for x in range (1, nr_nodes+1):
    G.add_node(x)

line = f2.readline()
while line:
    line = line.strip("\n")
    line = line.strip(' ')
    if line == "":
        break
    list = line.split(' ')
    x = int(list[0])
    list = list[2:]
    
    list = [x.split(",") for x in list]
    
    for [y,w] in list:
        y = int(y)
        w = int(w)
        
        G.add_weighted_edges_from([(x, y, w)])
        
    line = f2.readline()
    
# Find the MST for the graph using NetworkX.
T = nx.minimum_spanning_tree(G)
sorted_nx = sorted(T.edges(data=True))

# Find the MST calculated with your algorithm.
sorted_algo = set()
line = f.readline()
while line:
    [x,y] = [int(x) for x in line.strip().split()]
    
    sorted_algo.add((min(x,y), max(x,y)))
    line = f.readline()
sorted_algo = sorted(sorted_algo)

# Compare the 2
if len(sorted_nx) != len(sorted_algo):
    print("INCORRECT RESULT")
    correct = False
else:
    i = 0
    for y in sorted_algo:
        x = sorted_nx[i]
        
        if x[0] != y[0] or x[1] != y[1]:
            
            print("INCORRECT RESULT")
            correct = False
        i+=1
        
if correct == True:
    print("CORRECT MST")

