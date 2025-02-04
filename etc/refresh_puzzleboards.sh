#!/bin/bash

cd ~/src/github.com/klmcwhirter/python-projects/huntwords

if [ ! -d .venv ]
then
    echo 'Recreating .venv ...'
    pdm sync
fi

echo pdm manage puzzles
count=$(pdm manage puzzles | awk -F '=' '/^text=/ { print $2 }' | jq -c '.body | length')
echo count=${count}

if [ ${count} -lt 4 ]
then
    echo pdm manage puzzle_load --file ./etc/puzzles-all.json
    pdm manage puzzle_load --file ./etc/puzzles-all.json
fi

if [ "$1" = 'reload' ]
then
    echo pdm manage puzzleboards_clear
    pdm manage puzzleboards_clear
fi

MIN_PBS=5
puzzles=$(pdm manage puzzles | awk -F '=' '/^text=/ { print $2 }' | jq -cr .body[].name | sort)
for p in ${puzzles}
do
    count=$(pdm manage puzzleboard_count --name $p | awk -F '=' '/^text=/ { print $2 }' | jq -c '.body.count')
    need=$((MIN_PBS - count))
    over=$((count - MIN_PBS))
    echo $p count=${count}, need=${need}, over=${over}

    while [ $need -gt 0 ]
    do
        echo pdm manage puzzleboard_consume --name $p
        pdm manage puzzleboard_consume --name $p
        ((need -= 1))
    done

    while [ $over -gt 0 ]
    do
        echo pdm manage puzzleboard_pop --name $p
        pdm manage puzzleboard_pop --name $p
        ((over -= 1))
    done
done
