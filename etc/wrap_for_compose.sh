#!/bin/sh
#*----------------------------------------------------------------------*
#*
#* NAME: wrap_for_compose.sh
#*
#* DESCIPTION: Copy files needed for docker compose temporarily.
#*
#* The Docker build context has been constrained to a subdir. So copy files
#* needed from project root temporarily during build process.
#*----------------------------------------------------------------------*

function echo_eval
{
    # execute command being wrapped
    echo $*
    eval $*
}

#*----------------------------------------------------------------------*

DEST=api
FILES_TO_CP="pyproject.toml uv.lock .uvextras/"

function cleanup_files
{
    for f in ${FILES_TO_CP}
    do
        trg=${DEST}/${f}
        if [ -d ${trg} ]
        then
            echo_eval rm -fr $trg}
        else
            echo_eval rm ${trg}
        fi
    done
}

trap cleanup_files INT QUIT TERM EXIT

#*----------------------------------------------------------------------*

# copy files needed to build
echo_eval cp -v -r -t ${DEST} ${FILES_TO_CP}

echo_eval $*

#*----------------------------------------------------------------------*
