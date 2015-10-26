#!/bin/bash

#first we declare some variables
a=513
b=508

# Then we write an if statement
if [ "$a" = "$b" ]; then
    echo "expression evaluated as true"
else
    echo "expression evaluated as false"
fi

# We can also check if something is true or false like so:
# Then we write an if statement
vartrue=true
if [ "$vartrue" = true ]; then
    echo "expression evaluated as true"
else
    echo "expression evaluated as false"
fi

# if we want to check wether a string is unset (NULL) or empty ("") we use:
if [ -z "$UNSETVAR" ]; then
	echo "Variable is not set"
else
	echo "Variable is set"
fi

#other comparison Operators:

# -eq is equal to (also a = b  AND a == b)
if [ "$a" -eq "$b" ]; then
    echo "expression evaluated as true"
else
    echo "expression evaluated as false"
fi
 
# -ne Not Equal to (also a != b )
if [ "$a" -eq "$b" ]; then
    echo "expression evaluated as true"
else
    echo "expression evaluated as false"
fi

# -gt Greater Than
if [ "$a" -gt "$b" ]; then
    echo "expression evaluated as true"
else
    echo "expression evaluated as false"
fi 

# -gt Greater Than
if [ "$a" -gt "$b" ]; then
    echo "expression evaluated as true"
else
    echo "expression evaluated as false"
fi 

# -ge Greater than or Equal to
if [ "$a" -ge "$b" ]; then
    echo "expression evaluated as true"
else
    echo "expression evaluated as false"
fi 

# -lt Less Than
if [ "$a" -lt "$b" ]; then
    echo "expression evaluated as true"
else
    echo "expression evaluated as false"
fi 

# -le Less than or Equal to
if [ "$a" -lt "$b" ]; then
    echo "expression evaluated as true"
else
    echo "expression evaluated as false"
fi 
