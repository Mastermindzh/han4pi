#!/bin/bash

#Eerst maken we wat variabelen
a=513
b=508

# Vervolgens vergelijken we de waardes
if [ "$a" = "$b" ]; then
    echo "expression evaluated as true"
else
    echo "expression evaluated as false"
fi

# We kunnen ook kijken of iets waar of onwaar is met de volgende code:
vartrue=true
if [ "$vartrue" = true ]; then
    echo "expression evaluated as true"
else
    echo "expression evaluated as false"
fi

# Als we willen kijken of de string NULL of leeg is gebruiken we:
if [ -z "$UNSETVAR" ]; then
	echo "Variable is not set"
else
	echo "Variable is set"
fi

# Overige operators:

# -eq is equal to (also a = b  AND a == b)
# is gelijk aan
if [ "$a" -eq "$b" ]; then
    echo "expression evaluated as true"
else
    echo "expression evaluated as false"
fi
 
# -ne Not Equal to (also a != b )
# is niet gelijk aan
if [ "$a" -eq "$b" ]; then
    echo "expression evaluated as true"
else
    echo "expression evaluated as false"
fi

# -gt Greater Than
# - grooter dan
if [ "$a" -gt "$b" ]; then
    echo "expression evaluated as true"
else
    echo "expression evaluated as false"
fi 

# -ge Greater than or Equal to
# groter of gelijk aan
if [ "$a" -ge "$b" ]; then
    echo "expression evaluated as true"
else
    echo "expression evaluated as false"
fi 

# -lt Less Than
# minder dan
if [ "$a" -lt "$b" ]; then
    echo "expression evaluated as true"
else
    echo "expression evaluated as false"
fi 

# -le Less than or Equal to
# minder of gelijk aan
if [ "$a" -lt "$b" ]; then
    echo "expression evaluated as true"
else
    echo "expression evaluated as false"
fi 
