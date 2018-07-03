#!/bin/bash
# This script is for unary operator -nt(true if file 1 is newer than file 2 )
# Files are compared according  to modification date
clear
read -p 'Please enter any file name : ' file1
read -p 'Please enter another file name : ' file2
if [ ${file1} -nt ${file2} ]; then
	echo "File ${file1} is newer than ${file2}"
else
	echo "File ${file1} is older than ${file2}"
fi
