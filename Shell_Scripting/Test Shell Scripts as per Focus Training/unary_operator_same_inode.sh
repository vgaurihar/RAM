#!/bin/bash -x
# This script is for unary operator '-ef' means refer to same inode in same device
# (true if file 1 and file 2 refer to same inode and device )

clear
read -p 'Please enter any file name : ' file1
read -p 'Please enter another file name : ' file2
inod_num=`ls -l -i ${file1} | tr -s ' ' | cut -d ' ' -f1`
if [ ${file1} -ef ${file2} ]; then
	echo "File ${file1} and ${file2} have same inode number as : $inod_num "
else
	echo "File ${file1} and ${file2} have different inode numbers"
fi
