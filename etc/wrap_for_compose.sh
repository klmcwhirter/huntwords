#!/bin/bash
#*----------------------------------------------------------------------*
#*
#* NAME: wrap_for_compose.sh
#*
#* DESCIPTION: Copy files needed for docker compose temporarily.
#*
#* The Docker build context has been constrained to a subdir. So copy files
#* needed from project root temporarily during build process.
#*----------------------------------------------------------------------*

DEST=api
FILES_TO_CP="pdm.lock pyproject.toml"

function cleanup_files
{
    for f in ${FILES_TO_CP}
    do
        rm ${DEST}/${f}
    done
}

trap cleanup_files INT QUIT TERM EXIT

#*----------------------------------------------------------------------*

# copy files needed to build
cp -v -t ${DEST} ${FILES_TO_CP}

# execute command being wrapped
echo $*
eval $*

#*----------------------------------------------------------------------*
