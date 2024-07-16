#!/bin/bash

cd ~/src/github.com/klmcwhirter/python-projects/huntwords

if [ ! -d .venv ]
then
    echo 'Recreating .venv ...'
    pdm run create
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
puzzles=$(python -m manager puzzles | awk -F '=' '/^text=/ { print $2 }' | jq -cr .body[].name | sort)
for p in ${puzzles}
do
    count=$(python -m manager puzzleboard_count --name $p | awk -F '=' '/^text=/ { print $2 }' | jq -c '.body.count')
    need=$((MIN_PBS - count))
    over=$((count - MIN_PBS))
    echo $p count=${count}, need=${need}, over=${over}

    while [ $need -gt 0 ]
    do
        echo python -m manager puzzleboard_consume --name $p
        python -m manager puzzleboard_consume --name $p
        ((need -= 1))
    done

    while [ $over -gt 0 ]
    do
        echo python -m manager puzzleboard_pop --name $p
        python -m manager puzzleboard_pop --name $p
        ((over -= 1))
    done
done
