#!/bin/bash

#*--------------------------------------------------------------------------------*
function manage
{
    docker compose exec -t api uv run --frozen python -m api.manage $*
}
#*--------------------------------------------------------------------------------*

root_dir=$(dirname $(dirname $(realpath $0)))

cd ${root_dir}

if [ ! -d .venv ]
then
    echo 'Recreating .venv ...'
    uv sync --frozen
fi

manage puzzleboards | awk -F '=' '/^text=/ { print $2 }' | jq -Cr '.body.puzzleboards | to_entries[] | " \(.key): \(.value | length)"' | sort
