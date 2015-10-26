#!/bin/bash

#start while loop
while getopts 'hl' flag; do
  case "${flag}" in
    h) echo "This is the help menu" 
	flagDetection='true'
	exit 1;;
    l) 	cat ~/han4pi/LICENSE
	flagDetection='true' 
	exit 1;;
    *) echo "Unexpected option ${flag}" ;;
  esac
done



