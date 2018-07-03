from sys import argv

script, first, second, third = argv

print "The script is called: ", script
print "Your first variable is: ", first
print "Your second variable is:", second
print("Your third variable is: ", third)

# If I haven't pass any argument then it will give following error
# 'ValueError: need more than 1 value to unpack'

# If I pass 2 arguments then it will give following error
#ValueError: need more than 3 values to unpack

