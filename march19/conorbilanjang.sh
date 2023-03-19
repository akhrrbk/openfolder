#!/bin/bash

echo "Jangga tayyorlan. Birinchi bo'lib Conor bilan ringga tushasan. qaysi raqamni tanlaysan? (0/1)"
read userinput
conorBilan=$(( $RANDOM % 2 ))
sleep 1

echo "Jang ketyabdi!"
sleep 1
echo "*........."
sleep 1
echo "**........"
sleep 1
echo "***......."
sleep 2
echo "******...."
sleep 1
echo "********.."
sleep 1
echo "*********."
sleep 1
echo "**********"
sleep 1

if [[ $conorBilan == $userinput ]]; then
    echo "Olg'a bos, birinchi roundda sen yutyabsan!!!"
else
    echo "Birinchi rounddayoq nakautga uchrading!"
    exit 1
fi

sleep 2

echo "Ikkinchi roundga tayyorlan, nechchi raqamni tanlaysan? (0-9)"
read userinput
sleep 2

echo "Ozginadan keyin senga murabbiy Conorni kamchiligini aytib beradi, tayyor tur"
sleep 1
echo "*........."
sleep 1
echo "**........"
sleep 1
echo "***......."
sleep 2
echo "******...."
sleep 1
echo "********.."
sleep 1
echo "*********."
sleep 1
echo "**********"
sleep 1

randomNumber=$(( $RANDOM % 10 ))
if [[ $randomNumber -gt 5 ]];
then
    echo "5dan baland raqam ekan, OMAD!!!"
else
    echo "5 yoki past raqam ekan, OMAD!!!"
fi

echo "senda raqamni boshqatdan tanlash imkoniyati bor: "
read newUserinput
sleep 1

if [[ $newUserinput == $randomNumber ]];
then
    echo "Qoyil sen g'alaba qozonding!"
    sleep 1
    echo "Sen Conorni yutding!"
    sleep 1
    echo "Endi sen CHEMPION! $randonNumber"
else
    echo "Yutqazding, hech qisi yo'q. Keyingi safar urinib ko'r. $randomNumber"
    exit 1
fi