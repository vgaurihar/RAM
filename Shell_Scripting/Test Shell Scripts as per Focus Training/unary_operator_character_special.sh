#!/bin/bash
# This script is for unary operator '-c' (True if file exists and is a character special file.)
clear
read -p 'Please enter any file name : ' file1
if [ -c ${file1} ]; then
	echo -en "File ${file1} is Character special file \n`ls -l ${file1}`\n"
else
	echo "File ${file1} is not a Character special file"
	
fi
