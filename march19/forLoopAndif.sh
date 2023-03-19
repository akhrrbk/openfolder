#!/bin/bash
for n in 1 2 3 4 5 
	do
		if [ $n -eq 1 ] 
		then
			echo "$n second"
		fi

		if [ $n -gt 1 ]
		then 
			echo "$n seconds"
		fi
	sleep 1
	done