#!/bin/bash

rm -f colombia.json 

for place in $(cat colombia-lugares.txt); do
    echo "lugar: $place"
    for i in $(find -type f -iname '*.json'); do
	# echo "file: $i"
	loc="\"location\":\"$place\""
	lang="\"lang\":\"es\""
	# echo "$loc"
	grep -iE "$loc" $i | grep -iE "$lang" >> colombia.json
	# grep -iE "$loc" $i >> colombia.json
	# grep -iE "$loc" $i
    done
done
