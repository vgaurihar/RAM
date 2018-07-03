Python 2.7 (r27:82525, Jul  4 2010, 09:01:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 

>>> help(open)
Help on built-in function open in module __builtin__:

open(...)
    open(name[, mode[, buffering]]) -> file object
    
    Open a file using the file() type, returns a file object.  This is the
    preferred way to open a file.  See file.__doc__ for further information.

>>> open(r'D:\vaibhav passbook\IMAGE5.jpg')
<open file 'D:\vaibhav passbook\IMAGE5.jpg', mode 'r' at 0x0275A440>
>>> file_new = open(r'D:\vaibhav passbook\IMAGE5.jpg')
>>> file_new.name
'D:\\vaibhav passbook\\IMAGE5.jpg'
>>> file_new.
SyntaxError: invalid syntax
>>> file_new.close
<built-in method close of file object at 0x0275A180>
>>> file_new
<open file 'D:\vaibhav passbook\IMAGE5.jpg', mode 'r' at 0x0275A180>
>>> file_new.read
<built-in method read of file object at 0x0275A180>
>>> help(file_new.read)
Help on built-in function read:

read(...)
    read([size]) -> read at most size bytes, returned as a string.
    
    If the size argument is negative or omitted, read until EOF is reached.
    Notice that when in non-blocking mode, less data than what was requested
    may be returned, even if no size parameter was given.

>>> file_new.read()
'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x01\x00\xc8\x00\xc8\x00\x00\xff\xe2"\x14ICC_PROFILE\x00\x01\x01\x00\x00"\x04APPL\x02 \x00\x00mntrRGB XYZ \x07\xd6\x00\x02\x00\x02\x00\x02\x00\x14\x00\x00acspAPPL\x00\x00\x00\x00none\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf6\xd6\x00\x01\x00\x00\x00\x00\xd3-EPSO\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\ndesc\x00\x00!l\x00\x00\x00GrXYZ\x00\x00\x00\xfc\x00\x00\x00\x14gXYZ\x00\x00\x01\x10\x00\x00\x00\x14bXYZ\x00\x00\x01$\x00\x00\x00\x14wtpt\x00\x00\x018\x00\x00\x00\x14cprt\x00\x00!\xb4\x00\x00\x00PrTRC\x00\x00\x01L\x00\x00 \x0cgTRC\x00\x00\x01L\x00\x00 \x0cbTRC\x00\x00\x01L\x00\x00 \x0cbkpt\x00\x00!X\x00\x00\x00\x14XYZ \x00\x00\x00\x00\x00\x00o\xa2\x00\x008\xf5\x00\x00\x03\x90XYZ \x00\x00\x00\x00\x00\x00b\x99\x00\x00\xb7\x85\x00\x00\x18\xdaXYZ \x00\x00\x00\x00\x00\x00$\xa0\x00\x00\x0f\x84\x00\x00\xb6\xcfXYZ \x00\x00\x00\x00\x00\x00\xf3Q\x00\x01\x00\x00\x00\x01\x16\xcccurv\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x01\x00\x02\x00\x04\x00\x05\x00\x06\x00\x07\x00\t\x00\n\x00\x0b\x00\x0c\x00\x0e\x00\x0f\x00\x10\x00\x11\x00\x13\x00\x14\x00\x15\x00\x16\x00\x18\x00\x19\x00'
>>> file_new = open(r'D:\Jatin Sir Python Training\Test\Test3.txt')
>>> file_new
<open file 'D:\Jatin Sir Python Training\Test\Test3.txt', mode 'r' at 0x0275A440>
>>> file_new.read
<built-in method read of file object at 0x0275A440>
>>> file_new.read()
'!! Shriram Jai Ram Jai Jai Ram !!\n'
>>> help(file_new.read)
Help on built-in function read:

read(...)
    read([size]) -> read at most size bytes, returned as a string.
    
    If the size argument is negative or omitted, read until EOF is reached.
    Notice that when in non-blocking mode, less data than what was requested
    may be returned, even if no size parameter was given.

>>> file_new.read()
''
>>> file_new
<open file 'D:\Jatin Sir Python Training\Test\Test3.txt', mode 'r' at 0x0275A440>
>>> file_new.read()
''
>>> file_new = open(r'D:\Jatin Sir Python Training\Test\Test3.txt')
>>> file_new.read()
'!! Shriram Jai Ram Jai Jai Ram !!\n'
>>> file_new.read()
''
>>> file_new = open(r'D:\Jatin Sir Python Training\Test\Test3.txt')
>>> file_new.mode
'r'
>>> file_new.readline
<built-in method readline of file object at 0x0275A440>
>>> file_new.readline()
'!! Shriram Jai Ram Jai Jai Ram !!\n'
>>> file_new.readline()
''
>>> file_new = open(r'D:\Jatin Sir Python Training\Test\Test3.txt')
>>> help(file_new.readline)
Help on built-in function readline:

readline(...)
    readline([size]) -> next line from the file, as a string.
    
    Retain newline.  A non-negative size argument limits the maximum
    number of bytes to return (an incomplete line may be returned then).
    Return an empty string at EOF.

>>> file_new.readline(1)
'!'
>>> file_new.readline(1)
'!'
>>> file_new.readline(1)
' '
>>> file_new.readline(1)
'S'
>>> file_new.readline(1)
'h'
>>> file_new.readline(1)
'r'
>>> file_new.readline(1)
'i'
>>> file_new.readline(1)
'r'
>>> file_new.readline(1)
'a'
>>> file_new.readline(1)
'm'
>>> file_new.readline(1)
' '
>>> file_new.readline(1)
'J'
>>> file_new.readline()
'ai Ram Jai Jai Ram !!\n'
>>> help(file.new.readlines)

Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    help(file.new.readlines)
AttributeError: type object 'file' has no attribute 'new'
>>> help(file_new.readlines)
Help on built-in function readlines:

readlines(...)
    readlines([size]) -> list of strings, each a line from the file.
    
    Call readline() repeatedly and return a list of the lines so read.
    The optional size argument, if given, is an approximate bound on the
    total number of bytes in the lines returned.

>>> help(file_new.readline)
Help on built-in function readline:

readline(...)
    readline([size]) -> next line from the file, as a string.
    
    Retain newline.  A non-negative size argument limits the maximum
    number of bytes to return (an incomplete line may be returned then).
    Return an empty string at EOF.

>>> file_new.readlines()
[]
>>> file_new = open(r'D:\Jatin Sir Python Training\Test\Test3.txt')
>>> file_new.readlines(1)
['!! Shriram Jai Ram Jai Jai Ram !!\n']
>>> file_new = open(r'D:\Jatin Sir Python Training\Test\Test3.txt')
>>> file_new.readlines()
['!! Shriram Jai Ram Jai Jai Ram !!\n']
>>> file_new.close
<built-in method close of file object at 0x0275A180>
>>> file_new.close()
>>> file_new.read()

Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    file_new.read()
ValueError: I/O operation on closed file
>>> file_new = open(r'D:\Jatin Sir Python Training\Test\Test3.txt')
>>> file_new.read()
'!! Shriram Jai Ram Jai Jai Ram !!\n!! Shriram Jai Ram Jai Jai Ram !!\n!! Shriram Jai Ram Jai Jai Ram !!\n!! Shriram Jai Ram Jai Jai Ram !!\n!! Shriram Jai Ram Jai Jai Ram !!\n!! Shriram Jai Ram Jai Jai Ram !!\n!! Shriram Jai Ram Jai Jai Ram !!\n'
>>> file_new.close
<built-in method close of file object at 0x0275A440>
>>> file_new.close()
>>> file_new = open(r'D:\Jatin Sir Python Training\Test\Test3.txt')
>>> file_new.readlines()
['!! Shriram Jai Ram Jai Jai Ram !!\n', '!! Shriram Jai Ram Jai Jai Ram !!\n', '!! Shriram Jai Ram Jai Jai Ram !!\n', '!! Shriram Jai Ram Jai Jai Ram !!\n', '!! Shriram Jai Ram Jai Jai Ram !!\n', '!! Shriram Jai Ram Jai Jai Ram !!\n', '!! Shriram Jai Ram Jai Jai Ram !!\n']
>>> file_new.close()
>>> file_new = open(r'D:\Jatin Sir Python Training\Test\Test3.txt')
>>> file_new.readline([2])

Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    file_new.readline([2])
TypeError: an integer is required
>>> file_new.readline(2)
'!!'
>>> file_new.readlines(1)
[' Shriram Jai Ram Jai Jai Ram !!\n', '!! Shriram Jai Ram Jai Jai Ram !!\n', '!! Shriram Jai Ram Jai Jai Ram !!\n', '!! Shriram Jai Ram Jai Jai Ram !!\n', '!! Shriram Jai Ram Jai Jai Ram !!\n', '!! Shriram Jai Ram Jai Jai Ram !!\n', '!! Shriram Jai Ram Jai Jai Ram !!\n']
>>> file_new.readlines(-1)
[]
>>> file_new.readlines(0)
[]
>>> file_new.close()
>>> file_new = open(r'D:\Jatin Sir Python Training\Test\Test3.txt')
>>> file_new.readlines(0)
['!! Shriram Jai Ram Jai Jai Ram !!\n', '!! Shriram Jai Ram Jai Jai Ram !!\n', '!! Shriram Jai Ram Jai Jai Ram !!\n', '!! Shriram Jai Ram Jai Jai Ram !!\n', '!! Shriram Jai Ram Jai Jai Ram !!\n', '!! Shriram Jai Ram Jai Jai Ram !!\n', '!! Shriram Jai Ram Jai Jai Ram !!\n']
>>> file_new = open(r'D:\Jatin Sir Python Training\Test\Test3.txt')
>>> file_new.readlines(-1)
['!! Shriram Jai Ram Jai Jai Ram !!\n', '!! Shriram Jai Ram Jai Jai Ram !!\n', '!! Shriram Jai Ram Jai Jai Ram !!\n', '!! Shriram Jai Ram Jai Jai Ram !!\n', '!! Shriram Jai Ram Jai Jai Ram !!\n', '!! Shriram Jai Ram Jai Jai Ram !!\n', '!! Shriram Jai Ram Jai Jai Ram !!\n']
>>> file_new.readlines(-1)
[]
>>> file_new = open(r'D:\Jatin Sir Python Training\Test\Test3.txt')
>>> file_new.readline(0)
''
>>> file_new.readline(0)
''
>>> file_new.readline(0)
''
>>> file_new.readline(1)
'!'
>>> file_new.readline(0)
''
>>> file_new.readline(1)
'!'
>>> file_new.readline(1)
' '
>>> file_new.readline(1)
'S'
>>> file_new.readline(-1)
'hriram Jai Ram Jai Jai Ram !!\n'
>>> file_new.readline(1)
'!'
>>> file_new.readlines()[1]
'!! Shriram Jai Ram Jai Jai Ram !!\n'
>>> file_new.readlines()[2]

Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    file_new.readlines()[2]
IndexError: list index out of range
>>> file_new.readlines()[1]

Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    file_new.readlines()[1]
IndexError: list index out of range
>>> file_new = open(r'D:\Jatin Sir Python Training\Test\Test3.txt')
>>> file_new.readlines()[0]
'!! Shriram Jai Ram Jai Jai Ram !!\n'
>>> file_new.readlines()[1]

Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    file_new.readlines()[1]
IndexError: list index out of range
>>> file_new.close()
>>> file_new.open(r'D:\Jatin Sir Python Training\Test\Test3.txt')

Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    file_new.open(r'D:\Jatin Sir Python Training\Test\Test3.txt')
AttributeError: 'file' object has no attribute 'open'
>>> file_new = open(r'D:\Jatin Sir Python Training\Test\Test3.txt')
>>> file_new.readlines()[0]
'\xef\xbb\xbf!! Shriram Jai Ram Jai Jai Ram !! Line1\n'
>>> file_new.readlines()[0]

Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    file_new.readlines()[0]
IndexError: list index out of range
>>> file_new.readlines()[1]

Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    file_new.readlines()[1]
IndexError: list index out of range
>>> file_new.readlines()[-1]

Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    file_new.readlines()[-1]
IndexError: list index out of range
>>> file_new.readlines()[]
SyntaxError: invalid syntax
>>> file_new.readlines()[1]

Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    file_new.readlines()[1]
IndexError: list index out of range
>>> file_new.readlines()
[]
>>> file_new.open(r'D:\Jatin Sir Python Training\Test\Test3.txt')

Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    file_new.open(r'D:\Jatin Sir Python Training\Test\Test3.txt')
AttributeError: 'file' object has no attribute 'open'
>>> file_new =open(r'D:\Jatin Sir Python Training\Test\Test3.txt')
>>> file_new.readline()[1]
'\xbb'
>>> file_new.readline()[1]
'!'
>>> file_new.readline()
'!! Shriram Jai Ram Jai Jai Ram !! Line3\n'
>>> file_new.readline()
'!! Shriram Jai Ram Jai Jai Ram !! Line4\n'
>>> file_new.readline()[range(8,11)]

Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    file_new.readline()[range(8,11)]
TypeError: string indices must be integers, not list
>>> file_new.readline()[range(8)]

Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    file_new.readline()[range(8)]
TypeError: string indices must be integers, not list
>>> file_new.readline()[0]
'!'
>>> file_new.readline()[-1]

Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    file_new.readline()[-1]
IndexError: string index out of range
>>> file_new.readline()
''
>>> file_new = open(r'D:\Jatin Sir Python Training\Test\Test3.txt')
>>> file_new.readline()[8]
'r'
>>> help(os.path)

Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    help(os.path)
NameError: name 'os' is not defined
>>> import os
>>> help(os.path)
Help on module ntpath:

NAME
    ntpath - Common pathname manipulations, WindowsNT/95 version.

FILE
    c:\python27\lib\ntpath.py

DESCRIPTION
    Instead of importing this module directly, import os and refer to this
    module as os.path.

FUNCTIONS
    abspath(path)
        Return the absolute version of a path.
    
    basename(p)
        Returns the final component of a pathname
    
    commonprefix(m)
        Given a list of pathnames, returns the longest common leading component
    
    dirname(p)
        Returns the directory component of a pathname
    
    exists(path)
        Test whether a path exists.  Returns False for broken symbolic links
    
    expanduser(path)
        Expand ~ and ~user constructs.
        
        If user or $HOME is unknown, do nothing.
    
    expandvars(path)
        Expand shell variables of the forms $var, ${var} and %var%.
        
        Unknown variables are left unchanged.
    
    getatime(filename)
        Return the last access time of a file, reported by os.stat().
    
    getctime(filename)
        Return the metadata change time of a file, reported by os.stat().
    
    getmtime(filename)
        Return the last modification time of a file, reported by os.stat().
    
    getsize(filename)
        Return the size of a file, reported by os.stat().
    
    isabs(s)
        Test whether a path is absolute
    
    isdir(s)
        Return true if the pathname refers to an existing directory.
    
    isfile(path)
        Test whether a path is a regular file
    
    islink(path)
        Test for symbolic link.
        On WindowsNT/95 and OS/2 always returns false
    
    ismount(path)
        Test whether a path is a mount point (defined as root of drive)
    
    join(a, *p)
        Join two or more pathname components, inserting "\" as needed.
        If any component is an absolute path, all previous path components
        will be discarded.
    
    lexists = exists(path)
        Test whether a path exists.  Returns False for broken symbolic links
    
    normcase(s)
        Normalize case of pathname.
        
        Makes all characters lowercase and all slashes into backslashes.
    
    normpath(path)
        Normalize path, eliminating double slashes, etc.
    
    realpath = abspath(path)
        Return the absolute version of a path.
    
    relpath(path, start='.')
        Return a relative version of a path
    
    split(p)
        Split a pathname.
        
        Return tuple (head, tail) where tail is everything after the final slash.
        Either part may be empty.
    
    splitdrive(p)
        Split a pathname into drive and path specifiers. Returns a 2-tuple
        "(drive,path)";  either part may be empty
    
    splitext(p)
        Split the extension from a pathname.
        
        Extension is everything from the last dot to the end, ignoring
        leading dots.  Returns "(root, ext)"; ext may be empty.
    
    splitunc(p)
        Split a pathname into UNC mount point and relative path specifiers.
        
        Return a 2-tuple (unc, rest); either part may be empty.
        If unc is not empty, it has the form '//host/mount' (or similar
        using backslashes).  unc+rest is always the input path.
        Paths containing drive letters never have an UNC part.
    
    walk(top, func, arg)
        Directory tree walk with callback function.
        
        For each directory in the directory tree rooted at top (including top
        itself, but excluding '.' and '..'), call func(arg, dirname, fnames).
        dirname is the name of the directory, and fnames a list of the names of
        the files and subdirectories in dirname (excluding '.' and '..').  func
        may modify the fnames list in-place (e.g. via del or slice assignment),
        and walk will only recurse into the subdirectories whose names remain in
        fnames; this can be used to implement a filter, or to impose a specific
        order of visiting.  No semantics are defined for, or required of, arg,
        beyond that arg is always passed to func.  It can be used, e.g., to pass
        a filename pattern, or a mutable object designed to accumulate
        statistics.  Passing None for arg is common.

DATA
    __all__ = ['normcase', 'isabs', 'join', 'splitdrive', 'split', 'splite...
    altsep = '/'
    curdir = '.'
    defpath = r'.;C:\bin'
    devnull = 'nul'
    extsep = '.'
    pardir = '..'
    pathsep = ';'
    sep = r'\'
    supports_unicode_filenames = True


>>> help(os.path.exists)
Help on function exists in module genericpath:

exists(path)
    Test whether a path exists.  Returns False for broken symbolic links

>>> 
