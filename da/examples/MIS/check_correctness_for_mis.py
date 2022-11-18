f1 = open(r'/home/bianca/distAlgo/distalgo/da/examples/MIS/graph3.txt')
f2 = open(r'/home/bianca/distAlgo/distalgo/da/examples/MIS/found_mis.txt')

mis = []
line = f2.readline()
while line:
    line = line.strip('\n')
    mis.append(int(line))
    line = f2.readline()

line = f1.readline()
while line:
    line = line.strip('\n')
    list = line.split(' ')
    x = list[0]
    neigh = [int(x) for x in list[2:(-1)]]
    if x in mis:
        if any(y in mis for y in neigh):
            print("the mis is not correct: 2 neighbors in ")
    else:
        if all(y not in mis for y in neigh):
            print("the mis is not correct: this one has no neighbors")
    
    line = f1.readline()