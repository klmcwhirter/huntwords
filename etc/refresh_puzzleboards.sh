#!/bin/bash

root_dir=$(dirname $(dirname $(realpath $0)))

cd ${root_dir}

if [ ! -d .venv ]
then
    echo 'Recreating .venv ...'
    uvextras run create
fi

echo uvextras run manage -- puzzles
count=$(uvextras run manage -- puzzles | awk -F '=' '/^text=/ { print $2 }' | jq -c '.body | length')
echo count=${count}

if [ ${count} -lt 4 ]
then
    echo uvextras run manage -- puzzle_load --file ./etc/puzzles-all.json
    uvextras run manage -- puzzle_load --file ./etc/puzzles-all.json
fi

if [ "$1" = 'reload' ]
then
    echo uvextras run manage -- puzzleboards_clear
    uvextras run manage -- puzzleboards_clear
fi

MIN_PBS=5
puzzles=$(uvextras run manage -- puzzles | awk -F '=' '/^text=/ { print $2 }' | jq -cr .body[].name | sort)
for p in ${puzzles}
do
    count=$(uvextras run manage -- puzzleboard_count --name $p | awk -F '=' '/^text=/ { print $2 }' | jq -c '.body.count')
    need=$((MIN_PBS - count))
    over=$((count - MIN_PBS))
    echo $p count=${count}, need=${need}, over=${over}

    while [ $need -gt 0 ]
    do
        echo uvextras run manage -- puzzleboard_consume --name $p
        uvextras run manage -- puzzleboard_consume --name $p
        ((need -= 1))
    done

    while [ $over -gt 0 ]
    do
        echo uvextras run manage -- puzzleboard_pop --name $p
        uvextras run manage -- puzzleboard_pop --name $p
        ((over -= 1))
    done
done
