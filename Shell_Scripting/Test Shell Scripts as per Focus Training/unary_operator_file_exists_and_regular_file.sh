#!/bin/bash
# This script is for unary operator '-f' (True if file exists and it is regular file)
clear
read -p 'Please enter any file name : ' file1
if [ -f ${file1} ]; then
	echo -en "The filename you entered is exists and is regular file  \n`ls -l ${file1}`\n"
else
	echo "'${file1}' is not a regular file"
	
fi
