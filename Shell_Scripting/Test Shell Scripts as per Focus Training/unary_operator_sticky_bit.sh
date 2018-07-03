#!/bin/bash
# This script is for unary operator '-k' (True if file exists and its sticky bit is set)
clear
read -p 'Please enter any file name : ' file1
if [ -k ${file1} ]; then
	echo -en "The filename you entered is exists and its sticky bit is set  \n`ls -l ${file1}`\n"
else
	echo "The sticky bit is not set on '${file1}'"
	
fi
