#!/bin/bash

mkdir -p data

echo "Uncompressing tar files into data folder"
for i in *.tar; do
    echo "Uncompressing $i"
    mv $i data
    cd data
    tar -xvf $i
    mv $i ..
    cd ..
done

function dbzip () {
    echo "$1"
    bzip2 -d "$1"
}

export -f dbzip

echo "Uncompressing compressed json files"
SHELL=/bin/bash parallel dbzip ::: $(find -iname '*.bz2')

# find -iname '*.bz2' -exec sh -c "echo {} ; bzip2 -d {}" \;
# find -iname '*.bz2' -print -exec bzip2 -d {} +

echo "Program terminated ..."
