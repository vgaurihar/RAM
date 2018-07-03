#!/bin/bash

# ------------------------------------------

# let us learn what an "exit status" is

# ------------------------------------------

ls -l &> /dev/null

echo " After running ls -l, Value of exit status = $?"

ls -z &> /dev/null


echo " After running ls -z, Value of exit status = $?"

useradd shekhar &> /dev/null


echo " After running useradd, Value of exit status = $?"
