#!/bin/bash

s=9000
xterm -e "./chord.py $s" &
i=`expr $s + 1`
echo $s
echo $i
while [ "$i" -le "9020" ]
do
	sleep 2
	xterm -e "./chord.py $i localhost $s" &
	i=`expr $i + 1`
done
