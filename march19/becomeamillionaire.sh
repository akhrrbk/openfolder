#!/bin/bash

echo "what is your name?"
read name
sleep 1

echo "what is your age?"
read age
sleep 2

whenamirichcode=$((( $RANDOM % 10 ) + $age ))
echo "Hi $name. You will become a millionare at $whenamirich years old"
sleep 1