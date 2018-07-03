#!/bin/bash
# This script is for unary operator '-d' (True if it is a directory and it exists)
clear
read -p 'Please enter any directory name : ' dir1
if [ -d ${dir1} ]; then
	echo -en "The name you entered is a Directory ${dir1} \nThe content of which is ....\n`ls -l ${dir1}`\n"
else
	echo "'${dir1}' is not a directory"
	
fi
