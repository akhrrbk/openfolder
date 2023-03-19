#@/bin/bash

echo "hey, do you like coffee? [y/n]"
read answer

if [[ $answer == "y" || $answer == "Y" ]]; then
    echo "You're awesome"
else
    echo "Leave right now!!!"
fi