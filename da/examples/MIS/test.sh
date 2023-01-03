#!/bin/bash

for (( i=0; i<10; i++ ))
do
    for (( j = 0; j <10; j++))
    do
        python -m da lubys.da 1000 "$i" "$j"
        python -m da ghaffari.da 1000 "$i" "$j"
    done
done