#!/bin/bash

cd ~/src/github.com/klmcwhirter/python-projects/huntwords

if [ ! -d .venv ]
then
    echo 'Recreating .venv ...'
    ./create_venv >/dev/null
fi

source ./.venv/bin/activate

MIN_PBS=5
for p in Animals Bible Flowers Fruit
do
    count=$(python -m manager puzzleboard_count --name $p | awk -F '=' '/^text=/ { print $2 }' | jq -c '.body.count')
    need=$((MIN_PBS - count))
    echo $p count=${count}, need=${need}
    while [ $need -gt 0 ]
    do
        python -m manager puzzleboard_consume --name $p

        count=$(python -m manager puzzleboard_count --name $p | awk -F '=' '/^text=/ { print $2 }' | jq -c '.body.count')
        need=$((MIN_PBS - count))
    done
done
