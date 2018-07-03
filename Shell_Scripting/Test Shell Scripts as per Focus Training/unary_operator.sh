#!/bin/bash 
clear
read -p "Please enter any file or directory name :" fn
#set -x
if [ -a ${fn} -a -x ${fn} ]; then
	
	echo "The file or directory name you entered ${fn} is exist and executable"
	ls -lhtr ${fn} 2> /dev/null
else

	echo "The file or directory name you entered ${fn} does not exists"

	ls -lhtr ${fn} &> /dev/null
fi

#set +x
exit
RAM
