from os.path import exists
import time
time1 = time.time()
from_file = raw_input("Please enter file name whose data to be copied: ")
to_file = raw_input("Please enter file name where data to be copied: ")

print "checking whether both files are present or not"

if exists(from_file) and exists(to_file) == True:
    print "%r and %r exists" % (from_file, to_file)
else:
    print "Please check one of file is missing"

time2 = time.time()
print "total time required for running script", time2 - time1
    



