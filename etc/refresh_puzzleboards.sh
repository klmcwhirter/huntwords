#!/bin/bash

cd ~/src/github.com/klmcwhirter/python-projects/huntwords

if [ ! -d .venv ]
then
    echo 'Recreating .venv ...'
    ./create_venv >/dev/null
fi

source ./.venv/bin/activate

echo python -m manager puzzles
count=$(python -m manager puzzles | awk -F '=' '/^text=/ { print $2 }' | jq -c '.body | length')
echo count=${count}

if [ ${count} -lt 4 ]
then
    echo python -m manager puzzle_load --file ./files/puzzles-all.json
    python -m manager puzzle_load --file ./files/puzzles-all.json
fi

if [ "$1" = 'reload' ]
then
    echo python -m manager puzzleboards_clear
    python -m manager puzzleboards_clear
fi

MIN_PBS=5
for p in Animals Bible Flowers Fruit
do
    count=$(python -m manager puzzleboard_count --name $p | awk -F '=' '/^text=/ { print $2 }' | jq -c '.body.count')
    need=$((MIN_PBS - count))
    echo $p count=${count}, need=${need}
    while [ $need -gt 0 ]
    do
        echo python -m manager puzzleboard_consume --name $p
        python -m manager puzzleboard_consume --name $p

        count=$(python -m manager puzzleboard_count --name $p | awk -F '=' '/^text=/ { print $2 }' | jq -c '.body.count')
        need=$((MIN_PBS - count))
    done
done
