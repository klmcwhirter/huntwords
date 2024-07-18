#!/bin/bash

DIR=$(dirname $0)

cd ~/src/github.com/klmcwhirter/python-projects/huntwords

if [ ! -d .venv ]
then
    echo 'Recreating .venv ...'
    ./create_venv >/dev/null
fi

source ./.venv/bin/activate

count=$(python -m manager puzzles | awk -F '=' '/^text=/ { print $2 }' | jq -c '.body | length')
echo count=${count}

if [ "$1" = "reload" -o ${count} -ne 4 ]
then
    python -m manager puzzleboards_clear

    python -m manager puzzle_load --file ./etc/puzzles-all.json

    ${DIR}/refresh_puzzleboards.sh
fi
