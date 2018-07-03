
from os.path import exists
from_file = raw_input("Please enter file name to be copied with absolute path : ")
to_file = raw_input("Please enter file name where content to be copied with absolute path : ")
print "Copying content of file %r into file %r" %(from_file, to_file)
output = open(to_file, 'w').write(open(from_file).read())
print "Alright Done!"



