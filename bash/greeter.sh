#!/bin/bash
# Maak het scherm leeg
clear

# sla de datum op
h=`date +%H`
#Maak arrays van dagen en maanden
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


# Als het uur onder de 12 is dan is het sochtends
if [ $h -lt 12 ]; then
  echo "Goedemorgen, $(whoami)!"
# als het uur onder de 18 is (maar niet onder de 12) dan is het middag
elif [ $h -lt 18 ]; then
  echo "Goedemiddag, $(whoami)!"
# Anders is het savonds
else 
  echo "Goedeavond, $(whoami)!"
fi
echo ""
echo "Welkom bij het han4pi leerprogramma!"
echo "Hieronder staat vast wat belangrijke informatie."
# Horizontaal lijntje
printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' -

#vraag de datum op en zet er de dag in tekst voor
echo "Datum: ${DAYS[$(date +%u)]} $(date +%d) ${MONTHS[$(date +%m)]} $(date +%Y)"
echo ""
#haal het lokale ip op van de raspberry pi
echo "IP : $(ip route get 8.8.8.8 | awk 'NR==1 {print $NF}')"
#haal het vrije geheugen op
free -m | awk 'NR==2{printf "MEM: %s/%sMB (%.2f%%)\n", $3,$2,$3*100/$2 }'
#haal de vrije schijfruimte op
df -h | awk '$NF=="/"{printf "HDD: %d/%dGB (%s)\n", $3,$2,$5}'
#haal de cpu load op
top -bn1 | grep load | awk '{printf "CPU: %.2f\n", $(NF-2)}' 
