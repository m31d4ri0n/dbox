#!/bin/bash

list_of_mkv () {
	ls ./ |grep '.mkv'
}

ls ./ |grep '.mkv' > dlist.txt
cat dlist.txt | while read mkvs
do
	echo "Archiving $mkvs"
	tar -cvjf $mkvs

tar -cvjf filmss.tar ./* ;
bzip2 filmss.tar ;
split -d -a 4 -b 50M filmss.tar.bz2 "filmss.tar.bz2.part"


