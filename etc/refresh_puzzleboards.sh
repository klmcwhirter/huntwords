#!/bin/bash

PUZZLES_JSON='../etc/puzzles-all.json'

#*--------------------------------------------------------------------------------*
function manage
{
    if [ -z "${API_URL-}" ]
    then
        docker compose exec -t api uv run --frozen --directory src python -m manage $*
    else
        uvextras run api-manage -- $*
    fi
}
#*--------------------------------------------------------------------------------*

root_dir=$(dirname $(dirname $(realpath $0)))

cd ${root_dir}

echo manage -- puzzles
count=$(manage -- puzzles | awk -F '=' '/^text=/ { print $2 }' | jq -c '.body | length')
echo count=${count}

if [ ${count} -lt 4 ]
then
    echo manage -- puzzle_load --file "${PUZZLES_JSON}"
    manage -- puzzle_load --file "${PUZZLES_JSON}"
fi

if [ "$1" = 'reload' ]
then
    echo manage -- puzzleboards_clear
    manage -- puzzleboards_clear
fi

MIN_PBS=5
puzzles=$(manage -- puzzles | awk -F '=' '/^text=/ { print $2 }' | jq -cr .body[].name | sort)
for p in ${puzzles}
do
    count=$(manage -- puzzleboard_count --name $p | awk -F '=' '/^text=/ { print $2 }' | jq -c '.body.count')
    need=$((MIN_PBS - count))
    over=$((count - MIN_PBS))
    echo $p count=${count}, need=${need}, over=${over}

    while [ $need -gt 0 ]
    do
        echo manage -- puzzleboard_consume --name $p
        manage -- puzzleboard_consume --name $p
        ((need -= 1))
    done

    while [ $over -gt 0 ]
    do
        echo manage -- puzzleboard_pop --name $p
        manage -- puzzleboard_pop --name $p
        ((over -= 1))
    done
done

#*--------------------------------------------------------------------------------*
