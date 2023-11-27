#!/usr/bin/env bash
# This script will display a number from 1 - 20 with some intersections
# in between the numbers

a=1
while [ $a -le 20 ]
do
	if [ $a -eq 4 ]
	then
		echo "4"
		echo "bad luck for China"
	elif [ $a -eq 9 ]
	then
		echo "9"
		echo "bad luck for Japan"
	elif [ $a -eq 17 ]
	then
		echo "17"
		echo "bad luck for Italy"
	else
		echo $a
	fi
	a=$((a+1))
done

