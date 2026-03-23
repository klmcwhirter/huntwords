#!/bin/bash

root_dir=$(dirname $(dirname $(realpath $0)))

cd ${root_dir}

if [ ! -d .venv ]
then
    echo 'Recreating .venv ...'
    uv sync --frozen
fi

uvextras run manage -- puzzleboards | awk -F '=' '/^text=/ { print $2 }' | jq -Cr '.body.puzzleboards | to_entries[] | " \(.key): \(.value | length)"'
