import sys
import networkx as nx

nr_nodes = int(sys.argv[1])
which_graph = int(sys.argv[2])
which_run = int(sys.argv[3])

file = f"/home/bianca/licenta/distalgo/da/examples/demo/MIS/results/{which_run}/node_results.txt"
f = open(file)
graph = f"/home/bianca/licenta/distalgo/da/examples/MIS/graphs/{nr_nodes}/graph{which_graph}.txt"
f2 = open(graph)

correct = True

dict = {}
line = f2.readline()
n = 1
while line:
    line = line.strip("\n")
    list = line.split(' ')
    x = list[0]

    dict[n] = [int(x) for x in list[2:(-1)]]
    line = f2.readline()
    n += 1

mis = []

line = f.readline()
while line:
    line = line.strip("\n")
    list = line.split(' ')
    x = list[0]
    y = list[2]
    if y == "IN":
        mis.append(int(x))
    line = f.readline()
    
for key in dict.keys():
    all = False
    for value in dict[key]:
        a = key in mis
        b = value in mis
        all = all or b
        if a and b:
            correct = False
            print(f"THE MIS IS NOT RIGHT {mis} {key} {value}")
    if key not in mis and all == False:
        correct = False
        print(f"THE MIS IS NOT RIGHT: none of {key}'s neighbors ({dict[key]}) is in the mis {mis}")
            
if correct == True:
    print("CORRECT MIS")