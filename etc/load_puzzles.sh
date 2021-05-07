#!/bin/bash

python -m manager puzzle_load --file ./files/puzzles-all.json

for p in Animals Bible Flowers Fruit;do for ct in 1 2 3 4 5;do python -m manager puzzleboard_consume --name $p;sleep 2;done;done
