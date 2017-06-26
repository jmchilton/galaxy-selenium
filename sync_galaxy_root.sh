#!/bin/bash

usage() {
cat << EOF
Usage: ${0##*/} [-i] /path/to/galaxy...
Sync galaxy-selenium modules to those same modules in Galaxy directory (or vice versa if -i).

EOF
}

if [ $# -lt 1 ]; then
    usage
    exit 1
fi

invert=0
OPTIND=1
while getopts ":i" opt; do
    case "$opt" in
        h)
            usage
            exit 0
            ;;
        i)
            invert=1
            ;;
        '?')
            usage >&2
            exit 1
            ;;
    esac
done
shift "$((OPTIND-1))" # Shift off the options and optional --.

PROJECT_DIRECTORY="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
GALAXY_DIRECTORY=$1



if [ "$invert" -ne "1" ];
then

    rm -rf $GALAXY_DIRECTORY/test/galaxy_selenium
    cp -r $PROJECT_DIRECTORY/test/galaxy_selenium $GALAXY_TEST_DIR/test/galaxy_selenium
    
else

    rm -rf $PROJECT_DIRECTORY/galaxy_selenium/*
    cp -r $GALAXY_LDIRECTORY/test/galaxy_selenium $PROJECT_DIRECTORY/

fi
