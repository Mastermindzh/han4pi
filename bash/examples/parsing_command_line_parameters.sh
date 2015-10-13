#!/bin/bash
 
 #loop throught parameters and check for a,b or v
 # : is used to disable verbose output
while getopts ":abv" opt; do
  
  #start a case to determine what code to run.
  case $opt in
    #if argument a is passed run
    a)
      echo "-a was triggered, Parameter: $OPTARG" 
      ;;
    #if argument b is passed run
    b)
      echo "-b was triggered, Parameter: $OPTARG" 
	  ;;
    #if argument v is passed run
    v)
	  echo "-v was triggered, Parameter: $OPTARG"
	  ;;
    #if argument is not in our list of arguments (a,b and v)
    \?)
      echo "Invalid option: -$OPTARG" >&2
      exit 1
      ;;
  #end case
  esac
#end while
done
