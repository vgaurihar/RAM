#!/bin/bash
clear
read -p 'Please enter username to be added : ' u
useradd  -  $u &> /dev/null
a=`echo $?`
if [ $a -eq 0 ]; then
	echo "Your command runs successfully whose exit status is $a  and user $u has been added"
elif [ $a -eq 1 ]; then
	echo "can´t update password file, exit status is $a"
elif [ $a -eq 2 ]; then
	echo "invalid command syntax, exit status is $a"
elif [ $a -eq 3 ]; then
	echo "invalid argument to option, exit status is $a"
elif [ $a -eq 9 ]; then
	echo "username already in use, exit status is $a"
elif [ $a -eq 126 ]; then
	echo "Permission denied, exit status is $a"
elif [ $a -eq 127 ]; then
	echo "command not found, Please check your command in script line no.4, exit status is $a"
fi
exit 
