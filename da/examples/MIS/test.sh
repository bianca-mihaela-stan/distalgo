#!/bin/bash

for (( i=0; i<10; i++ ))
do
    for (( j = 0; j <10; j++))
    do
        python -m da lubys.da "/home/bianca/licenta/distalgo/da/examples/MIS/graphs/1000/graph$i.txt"
    done
done