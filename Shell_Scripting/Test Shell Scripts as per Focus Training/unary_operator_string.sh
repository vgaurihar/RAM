#!/bin/bash
# This script is for unary operator -z (true if string value is zero)
# It accept only null value and space character
clear
read -p 'Please enter any sting : ' str
if [ -z $str ]; then
	echo "Please enter some string... dont write null value"
else
	echo "Hello  $str"
fi
