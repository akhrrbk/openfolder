#!/bin/bash

date=$(date)
echo "Today is $date"

for x in namangan andijan tashkent seoul busan tokyo london newyork jeddah doha dubai;
do
    weather=$(curl -s http://wttr.in/$x?format=3)
    echo "The weather for $weather"
done