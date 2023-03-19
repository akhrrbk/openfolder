#1/bin/bash
x=1
while [[ x -le 100 ]]; do
    echo "you did $x pushups"
    (( x ++ ))
done