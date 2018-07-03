import os, os.path

dir_name = raw_input('Please enter dir name :')
os.chdir(dir_name)
allfiles = os.listdir(dir_name)
if file in allfiles:
    absfile = dir_name + '/' + file
    print absfile
    if os.path.isfile(absfile):
        if os.path.getsize(absfile):
            print 'File %s is not empty' %file
            pass
        else:
            print 'File %s is empty' %file
            os.remove(absfile)
            
