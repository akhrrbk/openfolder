#!/bin/bash

name=$1
surname=$2

user=$(whoami)
date=$(date)
whereami=$(pwd)

echo "good morning $name"
sleep 1
echo "$surname"
sleep 2

echo "you are currently logged in as $user and you are in $whereami directory at $date time"
sleep 1