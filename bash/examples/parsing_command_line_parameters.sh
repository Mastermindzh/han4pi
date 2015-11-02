#!/bin/bash
 
 #Kijk of de parameter a b of v is meegegven
 # : wordt gebruikt om verbose output tegen te gaan
while getopts ":abv" opt; do
  
  #Bekijk in een case statement welke code uitgevoerd moet worden
  case $opt in
    #als a is meegegeven dan doe:
    a)
      echo "-a is meegegeven, Parameter: $OPTARG" 
      ;;
    #als b is meegegeven dan doe:
    b)
      echo "-b is meegegeven, Parameter: $OPTARG" 
	  ;;
    #als v is meegegeven dan doe:
    v)
	  echo "-v is meegegeven, Parameter: $OPTARG"
	  ;;
    #als is not in our list of arguments (a,b and v)
    \?)
      echo "Invalid option: -$OPTARG" >&2
      exit 1
      ;;
  #end case
  esac
#end while
done
