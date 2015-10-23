#!/bin/bash
# Start with a fresh screen
clear

# Get the date
h=`date +%H`
#set up array of months and days
MONTHS=(NULL Januari Februari Maart April Mei Juni Juli Augustus September October November December)
DAYS=(NULL Maandag Dinsdag Woensdag Donderdag Vrijdag Zaterdag Zondag)


echo " _                   ___       _  "
echo "| |                 /   |     (_) "
echo "| |__   __ _ _ __  / /| |_ __  _  "
echo "| |_ \ / _' | |_ \/ /_| | |_ \| | "
echo "| | | | (_| | | | \___  | |_) | | "
echo "|_| |_|\__,_|_| |_|   |_/ .__/|_| "
echo "                        | |       "
echo "                        |_|       "


# if the hour (H) is lower than 12 it's morning
if [ $h -lt 12 ]; then
  echo "Goedemorgen, $(whoami)!"
# elseif hour is less than 18 (it's midday)
elif [ $h -lt 18 ]; then
  echo "Goedemiddag, $(whoami)!"
# if neither of those are true it's evening
else 
  echo "Goedeavond, $(whoami)!"
fi
echo ""
echo "Welkom bij het han4pi leerprogramma!"
echo "Hieronder staat vast wat belangrijke informatie."
echo "Om te zien wat ik allemaal kan doen typ je 'help'"
# draw a horizontal line
printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' -


echo "Datum: ${DAYS[$(date +%u)]} $(date +%d) ${MONTHS[$(date +%m)]} $(date +%Y)"
echo ""
echo "IP : $(hostname -i)"
free -m | awk 'NR==2{printf "MEM: %s/%sMB (%.2f%%)\n", $3,$2,$3*100/$2 }'
df -h | awk '$NF=="/"{printf "HDD: %d/%dGB (%s)\n", $3,$2,$5}'
top -bn1 | grep load | awk '{printf "CPU: %.2f\n", $(NF-2)}' 
