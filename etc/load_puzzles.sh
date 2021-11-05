#!/bin/bash

cd ~/src/github.com/klmcwhirter/python-projects/huntwords

source ./venv/bin/activate

count=$(python -m manager puzzles | awk -F '=' '/^text=/ { print $2 }' | jq -c 'length')
echo count=${count}

if [ "$1" != "reload" -o ${count} -ne 4 ]
then
    python -m manager puzzleboards_clear

    python -m manager puzzle_load --file ./files/puzzles-all.json

    for p in Animals Bible Flowers Fruit;do for ct in 1 2 3 4 5;do python -m manager puzzleboard_consume --name $p;sleep 2;done;done
fi
