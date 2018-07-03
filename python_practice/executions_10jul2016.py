Python 2.7 (r27:82525, Jul  4 2010, 09:01:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> 

>>> fuunc = lambda a, b, c: a * b * c
>>> func(1,2,3)

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    func(1,2,3)
NameError: name 'func' is not defined
>>> func = lambda a, b, c: a * b * c
>>> func(1,2,3)
6
>>> dir(list.count)
['__call__', '__class__', '__delattr__', '__doc__', '__format__', '__get__', '__getattribute__', '__hash__', '__init__', '__name__', '__new__', '__objclass__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
>>> list1 = ['ram', 'jatin']
>>> help(list1.count)
Help on built-in function count:

count(...)
    L.count(value) -> integer -- return number of occurrences of value

>>> help(list1.extend)
Help on built-in function extend:

extend(...)
    L.extend(iterable) -- extend list by appending elements from the iterable

>>> list1.append('ram1')
>>> list1
['ram', 'jatin', 'ram1']
>>> list1.extend('ram1')
>>> list1
['ram', 'jatin', 'ram1', 'r', 'a', 'm', '1']
>>> if 'swara' in list1:
	print list1.index()

	
>>> if 'ram' in list1:
	print list1.index()

	

Traceback (most recent call last):
  File "<pyshell#18>", line 2, in <module>
    print list1.index()
TypeError: index() takes at least 1 argument (0 given)
>>> help(list1.insert)
Help on built-in function insert:

insert(...)
    L.insert(index, object) -- insert object before index

>>> naems.insert(0, 'Shashi')

Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    naems.insert(0, 'Shashi')
NameError: name 'naems' is not defined
>>> list1.insert(0, 'Shashi')
>>> list1
['Shashi', 'ram', 'jatin', 'ram1', 'r', 'a', 'm', '1']
>>> list1.insert(100, 'Shashi')
>>> list1
['Shashi', 'ram', 'jatin', 'ram1', 'r', 'a', 'm', '1', 'Shashi']
>>> help(list1.pop)
Help on built-in function pop:

pop(...)
    L.pop([index]) -> item -- remove and return item at index (default last).
    Raises IndexError if list is empty or index is out of range.

>>> list1.pop()
'Shashi'
>>> list1
['Shashi', 'ram', 'jatin', 'ram1', 'r', 'a', 'm', '1']
>>> list1.remove('ram')
>>> list1
['Shashi', 'jatin', 'ram1', 'r', 'a', 'm', '1']
>>> list1.reverse()
>>> list1
['1', 'm', 'a', 'r', 'ram1', 'jatin', 'Shashi']
>>> list1.sort()
>>> list1
['1', 'Shashi', 'a', 'jatin', 'm', 'r', 'ram1']
>>> list1.sort(reverse=True)
>>> list1
['ram1', 'r', 'm', 'jatin', 'a', 'Shashi', '1']
>>> # sorts as per Ascii values
>>> names = ['ram', 'akshay', 'akash', 'jatin']
>>> names.sort()
>>> names.sort(key=str.upper)
>>> names
['akash', 'akshay', 'jatin', 'ram']
>>> # converts each elements in CAPS like AKASH, AKSHAY...
>>> # then it sorts as per CAPS characters ASCII values
>>> # and returns original values after sorting
>>> 
>>> name_salary = [['Jatin', 25000], ['Ram', 15000], ['Vijay', 20000]]
>>> def salary_sort(x):
	return x(1)

>>> # returns first element
>>> name_salary.sort(key=salary_sort)

Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    name_salary.sort(key=salary_sort)
  File "<pyshell#48>", line 2, in salary_sort
    return x(1)
TypeError: 'list' object is not callable
>>> name_salary.sort(key=salary_sort())

Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    name_salary.sort(key=salary_sort())
TypeError: salary_sort() takes exactly 1 argument (0 given)
>>> name_salary.sort(key=salary_sort)

Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    name_salary.sort(key=salary_sort)
  File "<pyshell#48>", line 2, in salary_sort
    return x(1)
TypeError: 'list' object is not callable
>>> names
['akash', 'akshay', 'jatin', 'ram']
>>> sorted(names)
['akash', 'akshay', 'jatin', 'ram']
>>> emp = [['Jatin', 25000, ['akash', 'ram']], ['Ram', 15000, ['ram', 'vijay', 'akshay']], ['Vijay', 20000]]
>>> help(sorted)
Help on built-in function sorted in module __builtin__:

sorted(...)
    sorted(iterable, cmp=None, key=None, reverse=False) --> new sorted list

>>> sorted(emp)
[['Jatin', 25000, ['akash', 'ram']], ['Ram', 15000, ['ram', 'vijay', 'akshay']], ['Vijay', 20000]]
>>> emp.sorted()

Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    emp.sorted()
AttributeError: 'list' object has no attribute 'sorted'
>>> sorted(emp, cmp=len(emp))

Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    sorted(emp, cmp=len(emp))
TypeError: 'int' object is not callable
>>> sorted(emp)
[['Jatin', 25000, ['akash', 'ram']], ['Ram', 15000, ['ram', 'vijay', 'akshay']], ['Vijay', 20000]]
>>> sorted(emp)
[['Jatin', 25000, ['akash', 'ram']], ['Ram', 15000, ['ram', 'vijay', 'akshay']], ['Vijay', 20000]]
>>> sorted(emp, reverse=True, key=lambda x: len(x))
[['Jatin', 25000, ['akash', 'ram']], ['Ram', 15000, ['ram', 'vijay', 'akshay']], ['Vijay', 20000]]
>>> sorted(emp, reverse=True, key=lambda x: len(x)[2])

Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    sorted(emp, reverse=True, key=lambda x: len(x)[2])
  File "<pyshell#63>", line 1, in <lambda>
    sorted(emp, reverse=True, key=lambda x: len(x)[2])
TypeError: 'int' object is not subscriptable
>>> sorted(emp, reverse=True, key=lambda x: len(x)[0][0])

Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    sorted(emp, reverse=True, key=lambda x: len(x)[0][0])
  File "<pyshell#64>", line 1, in <lambda>
    sorted(emp, reverse=True, key=lambda x: len(x)[0][0])
TypeError: 'int' object is not subscriptable
>>> sorted(emp, reverse=True, key=lambda x: len(x[2]))

Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    sorted(emp, reverse=True, key=lambda x: len(x[2]))
  File "<pyshell#65>", line 1, in <lambda>
    sorted(emp, reverse=True, key=lambda x: len(x[2]))
IndexError: list index out of range
>>> sorted(emp, reverse=True, key=lambda x: len(x[1]))

Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    sorted(emp, reverse=True, key=lambda x: len(x[1]))
  File "<pyshell#66>", line 1, in <lambda>
    sorted(emp, reverse=True, key=lambda x: len(x[1]))
TypeError: object of type 'int' has no len()
>>> sorted(emp, reverse=True, key=lambda x: len(x[0]))
[['Jatin', 25000, ['akash', 'ram']], ['Vijay', 20000], ['Ram', 15000, ['ram', 'vijay', 'akshay']]]
>>> sorted(emp, reverse=True, key=lambda x: len(x[0][0][0]))
[['Jatin', 25000, ['akash', 'ram']], ['Ram', 15000, ['ram', 'vijay', 'akshay']], ['Vijay', 20000]]
>>> sorted(emp, reverse=True, key=lambda x: len(x[0]))
[['Jatin', 25000, ['akash', 'ram']], ['Vijay', 20000], ['Ram', 15000, ['ram', 'vijay', 'akshay']]]
>>> 
>>> 
>>> 




>>> 

>>> 


>>> 


>>> 


>>> 


>>> 


>>> 


>>> 


>>> 


>>> 


>>> 


>>> 


>>> # sorted with dictoinary
>>> #
>>> 
>>> 
>>> 

>>> 
>>> help(open)
Help on built-in function open in module __builtin__:

open(...)
    open(name[, mode[, buffering]]) -> file object
    
    Open a file using the file() type, returns a file object.  This is the
    preferred way to open a file.  See file.__doc__ for further information.

>>> fileObj = open()

Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    fileObj = open()
TypeError: Required argument 'name' (pos 1) not found
>>> 
>>> 




>>> 

>>> 


>>> 


>>> 



>>> 

>>> 


>>> 


>>> 

>>> file.open(r'C:\Users\RAM\Documents')

Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    file.open(r'C:\Users\RAM\Documents')
AttributeError: type object 'file' has no attribute 'open'
>>> open(r'C:\Users\RAM\Documents')

Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    open(r'C:\Users\RAM\Documents')
IOError: [Errno 13] Permission denied: 'C:\\Users\\RAM\\Documents'
>>> fileObj = open(r'C:\Users\RAM\Documents')

Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    fileObj = open(r'C:\Users\RAM\Documents')
IOError: [Errno 13] Permission denied: 'C:\\Users\\RAM\\Documents'
>>> fileObj = open(r'C:\Users\RAM\Documents', w)

Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    fileObj = open(r'C:\Users\RAM\Documents', w)
NameError: name 'w' is not defined
>>> fileObj = open(r'C:\Users\RAM\Documents', w)
KeyboardInterrupt
>>> 
>>> 
>>> 

>>> 
>>> fileObj = open(r'C:\Users\RAM\Documents',r+)
SyntaxError: invalid syntax
>>> fileObj = open(r'C:\Users\RAM\Documents',r)

Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    fileObj = open(r'C:\Users\RAM\Documents',r)
NameError: name 'r' is not defined
>>> fileObj = open(r'C:\Users\RAM\Documents')

Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    fileObj = open(r'C:\Users\RAM\Documents')
IOError: [Errno 13] Permission denied: 'C:\\Users\\RAM\\Documents'
>>> fileObj = open(r'C:\Users\RAM\Documents', 'r+')

Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    fileObj = open(r'C:\Users\RAM\Documents', 'r+')
IOError: [Errno 13] Permission denied: 'C:\\Users\\RAM\\Documents'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 

>>> 
>>> func = lambda x,y,z : x * Y * z
>>> func(1,2,3)

Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    func(1,2,3)
  File "<pyshell#123>", line 1, in <lambda>
    func = lambda x,y,z : x * Y * z
NameError: global name 'Y' is not defined
>>> func = lambda x,y,z : x * y * z
>>> func(1,2,3)
6
>>> func(1,2,3)
6
>>> func = lambda x,y,z: if x < y : print z
SyntaxError: invalid syntax
>>> func = lambda x,y,z: if x < y ; print z
SyntaxError: invalid syntax
>>> func = lambda x,y,z: if x < y
SyntaxError: invalid syntax
>>> func = lambda x,y,z:
	
SyntaxError: invalid syntax
>>> func = lambda x,y,z: x * y * z
>>> func(1,2,3)
6
>>> func = lambda x,y,z: x * y / z
>>> func(1,1,2)
0
>>> func(2,3,1)
6
>>> func = lambda x,y: if x < y; print y
SyntaxError: invalid syntax
>>> func = lambda x,y: if x < y
SyntaxError: invalid syntax
>>> help(if)
SyntaxError: invalid syntax
>>> help()

Welcome to Python 2.7!  This is the online help utility.

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at http://docs.python.org/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, or topics, type "modules",
"keywords", or "topics".  Each module also comes with a one-line summary
of what it does; to list the modules whose summaries contain a given word
such as "spam", type "modules spam".

help> if
The ``if`` statement
********************

The ``if`` statement is used for conditional execution:

   if_stmt ::= "if" expression ":" suite
               ( "elif" expression ":" suite )*
               ["else" ":" suite]

It selects exactly one of the suites by evaluating the expressions one
by one until one is found to be true (see section *Boolean operations*
for the definition of true and false); then that suite is executed
(and no other part of the ``if`` statement is executed or evaluated).
If all expressions are false, the suite of the ``else`` clause, if
present, is executed.

Related help topics: TRUTHVALUE

help> quit

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
>>> func = lambda x,y: if x<y: print y : else print x
SyntaxError: invalid syntax
>>> func = lambda x, y : x + y
>>> func(1,2)
3
>>> names = ['jatin', 'ram', 'vaibhav']
>>> help(names.append)
Help on built-in function append:

append(...)
    L.append(object) -- append object to end

>>> names.append('akash', 'akshay')

Traceback (most recent call last):
  File "<pyshell#146>", line 1, in <module>
    names.append('akash', 'akshay')
TypeError: append() takes exactly one argument (2 given)
>>> names.append('akash')
>>> names
['jatin', 'ram', 'vaibhav', 'akash']
>>> names.append('akash')
>>> names
['jatin', 'ram', 'vaibhav', 'akash', 'akash']
>>> names.append(names)
>>> names
['jatin', 'ram', 'vaibhav', 'akash', 'akash', [...]]
>>> 
>>> 
>>> names[6]

Traceback (most recent call last):
  File "<pyshell#155>", line 1, in <module>
    names[6]
IndexError: list index out of range
>>> names[5]
['jatin', 'ram', 'vaibhav', 'akash', 'akash', [...]]
>>> names[4]
'akash'
>>> names[4,5]

Traceback (most recent call last):
  File "<pyshell#158>", line 1, in <module>
    names[4,5]
TypeError: list indices must be integers, not tuple
>>> names[5][0]
'jatin'
>>> names[5][1]
'ram'
>>> names[5][3]
'akash'
>>> names[5][3]
'akash'
>>> names.insert(1)

Traceback (most recent call last):
  File "<pyshell#163>", line 1, in <module>
    names.insert(1)
TypeError: insert() takes exactly 2 arguments (1 given)
>>> help(names.insert)
Help on built-in function insert:

insert(...)
    L.insert(index, object) -- insert object before index

>>> names.insert(1, 2)
>>> names
['jatin', 2, 'ram', 'vaibhav', 'akash', 'akash', [...]]
>>> help(names.count)
Help on built-in function count:

count(...)
    L.count(value) -> integer -- return number of occurrences of value

>>> names.count('harish')
0
>>> names.count('ram')
1
>>> names.append('ram')
>>> names.append('ram')
>>> names
['jatin', 2, 'ram', 'vaibhav', 'akash', 'akash', [...], 'ram', 'ram']
>>> names.count('ram')
3
>>> help(names.extend)
Help on built-in function extend:

extend(...)
    L.extend(iterable) -- extend list by appending elements from the iterable

>>> names.extend('ram')
>>> names
['jatin', 2, 'ram', 'vaibhav', 'akash', 'akash', [...], 'ram', 'ram', 'r', 'a', 'm']
>>> len(names)
12
>>> names.index('jatin')
0
>>> names.index('ram')
2
>>> help(names.index)
Help on built-in function index:

index(...)
    L.index(value, [start, [stop]]) -> integer -- return first index of value.
    Raises ValueError if the value is not present.

>>> if 'swara' in names:
	print true

	
>>> names.insert('swara')

Traceback (most recent call last):
  File "<pyshell#184>", line 1, in <module>
    names.insert('swara')
TypeError: insert() takes exactly 2 arguments (1 given)
>>> names.insert(5.'swara')
SyntaxError: invalid syntax
>>> names.insert(5. 'swara')
SyntaxError: invalid syntax
>>> names.extend('swara')
>>> names
['jatin', 2, 'ram', 'vaibhav', 'akash', 'akash', [...], 'ram', 'ram', 'r', 'a', 'm', 's', 'w', 'a', 'r', 'a']
>>> if 'swara' in names:
	names.index()

	
>>> if 'swara' in names:
	print names.index()

	
>>> a = 'swara'
>>> names.extend(a)
>>> names
['jatin', 2, 'ram', 'vaibhav', 'akash', 'akash', [...], 'ram', 'ram', 'r', 'a', 'm', 's', 'w', 'a', 'r', 'a', 's', 'w', 'a', 'r', 'a']
>>> help(names.insert)
Help on built-in function insert:

insert(...)
    L.insert(index, object) -- insert object before index

>>> names.insert(1, 'swara')
>>> names
['jatin', 'swara', 2, 'ram', 'vaibhav', 'akash', 'akash', [...], 'ram', 'ram', 'r', 'a', 'm', 's', 'w', 'a', 'r', 'a', 's', 'w', 'a', 'r', 'a']
>>> names.pop()
'a'
>>> names.pop()
'r'
>>> names.pop()
'a'
>>> names.pop()
'w'
>>> names.pop()
's'
>>> names
['jatin', 'swara', 2, 'ram', 'vaibhav', 'akash', 'akash', [...], 'ram', 'ram', 'r', 'a', 'm', 's', 'w', 'a', 'r', 'a']
>>> names.pop(0, 1, 2, 3, 4)

Traceback (most recent call last):
  File "<pyshell#205>", line 1, in <module>
    names.pop(0, 1, 2, 3, 4)
TypeError: pop() takes at most 1 argument (5 given)
>>> names.pop(0)
'jatin'
>>> names
['swara', 2, 'ram', 'vaibhav', 'akash', 'akash', [...], 'ram', 'ram', 'r', 'a', 'm', 's', 'w', 'a', 'r', 'a']
>>> if 'swara' in names:
	print names.index()

	

Traceback (most recent call last):
  File "<pyshell#209>", line 2, in <module>
    print names.index()
TypeError: index() takes at least 1 argument (0 given)
>>> if 'swara' in names:
	print names.index('swara')

	
0
>>> 
>>> 


>>> 

>>> 



>>> 

>>> 


>>> 


>>> 

>>> 
>>> 
>>> 

>>> 

>>> 
>>> 
>>> 
>>> 

>>> 
>>> 

>>> 
>>> 
>>> 
>>> 

>>> 
>>> import math
>>> print math.__file__

Traceback (most recent call last):
  File "<pyshell#236>", line 1, in <module>
    print math.__file__
AttributeError: 'module' object has no attribute '__file__'
>>> import random
>>> print random.__file__
C:\Python27\lib\random.pyc
>>> from math import pi
>>> pi
3.141592653589793
>>> from math import pi, floor, factorial
>>> factorial(10)
3628800
>>> from math import *
>>> # this should be avoidable
>>> 
>>> 
>>> import sys
>>> help(sys)
Help on built-in module sys:

NAME
    sys

FILE
    (built-in)

MODULE DOCS
    http://docs.python.org/library/sys

DESCRIPTION
    This module provides access to some objects used or maintained by the
    interpreter and to functions that interact strongly with the interpreter.
    
    Dynamic objects:
    
    argv -- command line arguments; argv[0] is the script pathname if known
    path -- module search path; path[0] is the script directory, else ''
    modules -- dictionary of loaded modules
    
    displayhook -- called to show results in an interactive session
    excepthook -- called to handle any uncaught exception other than SystemExit
      To customize printing in an interactive session or to install a custom
      top-level exception handler, assign other functions to replace these.
    
    exitfunc -- if sys.exitfunc exists, this routine is called when Python exits
      Assigning to sys.exitfunc is deprecated; use the atexit module instead.
    
    stdin -- standard input file object; used by raw_input() and input()
    stdout -- standard output file object; used by the print statement
    stderr -- standard error object; used for error messages
      By assigning other file objects (or objects that behave like files)
      to these, it is possible to redirect all of the interpreter's I/O.
    
    last_type -- type of last uncaught exception
    last_value -- value of last uncaught exception
    last_traceback -- traceback of last uncaught exception
      These three are only available in an interactive session after a
      traceback has been printed.
    
    exc_type -- type of exception currently being handled
    exc_value -- value of exception currently being handled
    exc_traceback -- traceback of exception currently being handled
      The function exc_info() should be used instead of these three,
      because it is thread-safe.
    
    Static objects:
    
    float_info -- a dict with information about the float inplementation.
    long_info -- a struct sequence with information about the long implementation.
    maxint -- the largest supported integer (the smallest is -maxint-1)
    maxsize -- the largest supported length of containers.
    maxunicode -- the largest supported character
    builtin_module_names -- tuple of module names built into this interpreter
    version -- the version of this interpreter as a string
    version_info -- version information as a named tuple
    hexversion -- version information encoded as a single integer
    copyright -- copyright notice pertaining to this interpreter
    platform -- platform identifier
    executable -- pathname of this Python interpreter
    prefix -- prefix used to find the Python library
    exec_prefix -- prefix used to find the machine-specific Python library
    float_repr_style -- string indicating the style of repr() output for floats
    dllhandle -- [Windows only] integer handle of the Python DLL
    winver -- [Windows only] version number of the Python DLL
    __stdin__ -- the original stdin; don't touch!
    __stdout__ -- the original stdout; don't touch!
    __stderr__ -- the original stderr; don't touch!
    __displayhook__ -- the original displayhook; don't touch!
    __excepthook__ -- the original excepthook; don't touch!
    
    Functions:
    
    displayhook() -- print an object to the screen, and save it in __builtin__._
    excepthook() -- print an exception and its traceback to sys.stderr
    exc_info() -- return thread-safe information about the current exception
    exc_clear() -- clear the exception state for the current thread
    exit() -- exit the interpreter by raising SystemExit
    getdlopenflags() -- returns flags to be used for dlopen() calls
    getprofile() -- get the global profiling function
    getrefcount() -- return the reference count for an object (plus one :-)
    getrecursionlimit() -- return the max recursion depth for the interpreter
    getsizeof() -- return the size of an object in bytes
    gettrace() -- get the global debug tracing function
    setcheckinterval() -- control how often the interpreter checks for events
    setdlopenflags() -- set the flags to be used for dlopen() calls
    setprofile() -- set the global profiling function
    setrecursionlimit() -- set the max recursion depth for the interpreter
    settrace() -- set the global debug tracing function

FUNCTIONS
    __displayhook__ = displayhook(...)
        displayhook(object) -> None
        
        Print an object to sys.stdout and also save it in __builtin__._
    
    __excepthook__ = excepthook(...)
        excepthook(exctype, value, traceback) -> None
        
        Handle an exception by displaying it with a traceback on sys.stderr.
    
    call_tracing(...)
        call_tracing(func, args) -> object
        
        Call func(*args), while tracing is enabled.  The tracing state is
        saved, and restored afterwards.  This is intended to be called from
        a debugger from a checkpoint, to recursively debug some other code.
    
    callstats(...)
        callstats() -> tuple of integers
        
        Return a tuple of function call statistics, if CALL_PROFILE was defined
        when Python was built.  Otherwise, return None.
        
        When enabled, this function returns detailed, implementation-specific
        details about the number of function calls executed. The return value is
        a 11-tuple where the entries in the tuple are counts of:
        0. all function calls
        1. calls to PyFunction_Type objects
        2. PyFunction calls that do not create an argument tuple
        3. PyFunction calls that do not create an argument tuple
           and bypass PyEval_EvalCodeEx()
        4. PyMethod calls
        5. PyMethod calls on bound methods
        6. PyType calls
        7. PyCFunction calls
        8. generator calls
        9. All other calls
        10. Number of stack pops performed by call_function()
    
    displayhook(...)
        displayhook(object) -> None
        
        Print an object to sys.stdout and also save it in __builtin__._
    
    exc_clear(...)
        exc_clear() -> None
        
        Clear global information on the current exception.  Subsequent calls to
        exc_info() will return (None,None,None) until another exception is raised
        in the current thread or the execution stack returns to a frame where
        another exception is being handled.
    
    exc_info(...)
        exc_info() -> (type, value, traceback)
        
        Return information about the most recent exception caught by an except
        clause in the current stack frame or in an older stack frame.
    
    excepthook(...)
        excepthook(exctype, value, traceback) -> None
        
        Handle an exception by displaying it with a traceback on sys.stderr.
    
    exit(...)
        exit([status])
        
        Exit the interpreter by raising SystemExit(status).
        If the status is omitted or None, it defaults to zero (i.e., success).
        If the status is numeric, it will be used as the system exit status.
        If it is another kind of object, it will be printed and the system
        exit status will be one (i.e., failure).
    
    getcheckinterval(...)
        getcheckinterval() -> current check interval; see setcheckinterval().
    
    getdefaultencoding(...)
        getdefaultencoding() -> string
        
        Return the current default string encoding used by the Unicode 
        implementation.
    
    getfilesystemencoding(...)
        getfilesystemencoding() -> string
        
        Return the encoding used to convert Unicode filenames in
        operating system filenames.
    
    getprofile(...)
        getprofile()
        
        Return the profiling function set with sys.setprofile.
        See the profiler chapter in the library manual.
    
    getrecursionlimit(...)
        getrecursionlimit()
        
        Return the current value of the recursion limit, the maximum depth
        of the Python interpreter stack.  This limit prevents infinite
        recursion from causing an overflow of the C stack and crashing Python.
    
    getrefcount(...)
        getrefcount(object) -> integer
        
        Return the reference count of object.  The count returned is generally
        one higher than you might expect, because it includes the (temporary)
        reference as an argument to getrefcount().
    
    getsizeof(...)
        getsizeof(object, default) -> int
        
        Return the size of object in bytes.
    
    gettrace(...)
        gettrace()
        
        Return the global debug tracing function set with sys.settrace.
        See the debugger chapter in the library manual.
    
    getwindowsversion(...)
        getwindowsversion()
        
        Return information about the running version of Windows as a named tuple.
        The members are named: major, minor, build, platform, service_pack,
        service_pack_major, service_pack_minor, suite_mask, and product_type. For
        backward compatibiliy, only the first 5 items are available by indexing.
        All elements are numbers, except service_pack which is a string. Platform
        may be 0 for win32s, 1 for Windows 9x/ME, 2 for Windows NT/2000/XP/Vista/7,
        3 for Windows CE. Product_type may be 1 for a workstation, 2 for a domain
        controller, 3 for a server.
    
    setcheckinterval(...)
        setcheckinterval(n)
        
        Tell the Python interpreter to check for asynchronous events every
        n instructions.  This also affects how often thread switches occur.
    
    setprofile(...)
        setprofile(function)
        
        Set the profiling function.  It will be called on each function call
        and return.  See the profiler chapter in the library manual.
    
    setrecursionlimit(...)
        setrecursionlimit(n)
        
        Set the maximum depth of the Python interpreter stack to n.  This
        limit prevents infinite recursion from causing an overflow of the C
        stack and crashing Python.  The highest possible limit is platform-
        dependent.
    
    settrace(...)
        settrace(function)
        
        Set the global debug tracing function.  It will be called on each
        function call.  See the debugger chapter in the library manual.

DATA
    __stderr__ = <open file '<stderr>', mode 'w'>
    __stdin__ = <open file '<stdin>', mode 'r'>
    __stdout__ = <open file '<stdout>', mode 'w'>
    api_version = 1013
    argv = ['']
    builtin_module_names = ('__builtin__', '__main__', '_ast', '_bisect', ...
    byteorder = 'little'
    copyright = 'Copyright (c) 2001-2010 Python Software Foundati...ematis...
    dllhandle = 503316480
    dont_write_bytecode = False
    exc_value = Empty()
    exec_prefix = r'C:\Python27'
    executable = r'C:\Python27\pythonw.exe'
    flags = sys.flags(debug=0, py3k_warning=0, division_warn...abcheck=0, ...
    float_info = sys.float_info(max=1.7976931348623157e+308, max_...epsilo...
    float_repr_style = 'short'
    hexversion = 34013424
    last_value = AttributeError("'module' object has no attribute '__file_...
    long_info = sys.long_info(bits_per_digit=15, sizeof_digit=2)
    maxint = 2147483647
    maxsize = 2147483647
    maxunicode = 65535
    meta_path = []
    modules = {'ConfigParser': <module 'ConfigParser' from 'C:\Python27\li...
    path = [r'C:\Python27\Lib\idlelib', r'C:\Windows\system32\python27.zip...
    path_hooks = [<type 'zipimport.zipimporter'>]
    path_importer_cache = {'': None, r'C:\Python27': None, r'C:\Python27\D...
    platform = 'win32'
    prefix = r'C:\Python27'
    py3kwarning = False
    stderr = <idlelib.rpc.RPCProxy object>
    stdin = <idlelib.rpc.RPCProxy object>
    stdout = <idlelib.rpc.RPCProxy object>
    subversion = ('CPython', 'tags/r27', '82525')
    version = '2.7 (r27:82525, Jul  4 2010, 09:01:59) [MSC v.1500 32 bit (...
    version_info = sys.version_info(major=2, minor=7, micro=0, releaseleve...
    warnoptions = []
    winver = '2.7'


>>> import os
>>> dir(os)
['F_OK', 'O_APPEND', 'O_BINARY', 'O_CREAT', 'O_EXCL', 'O_NOINHERIT', 'O_RANDOM', 'O_RDONLY', 'O_RDWR', 'O_SEQUENTIAL', 'O_SHORT_LIVED', 'O_TEMPORARY', 'O_TEXT', 'O_TRUNC', 'O_WRONLY', 'P_DETACH', 'P_NOWAIT', 'P_NOWAITO', 'P_OVERLAY', 'P_WAIT', 'R_OK', 'SEEK_CUR', 'SEEK_END', 'SEEK_SET', 'TMP_MAX', 'UserDict', 'W_OK', 'X_OK', '_Environ', '__all__', '__builtins__', '__doc__', '__file__', '__name__', '__package__', '_copy_reg', '_execvpe', '_exists', '_exit', '_get_exports_list', '_make_stat_result', '_make_statvfs_result', '_pickle_stat_result', '_pickle_statvfs_result', 'abort', 'access', 'altsep', 'chdir', 'chmod', 'close', 'closerange', 'curdir', 'defpath', 'devnull', 'dup', 'dup2', 'environ', 'errno', 'error', 'execl', 'execle', 'execlp', 'execlpe', 'execv', 'execve', 'execvp', 'execvpe', 'extsep', 'fdopen', 'fstat', 'fsync', 'getcwd', 'getcwdu', 'getenv', 'getpid', 'isatty', 'kill', 'linesep', 'listdir', 'lseek', 'lstat', 'makedirs', 'mkdir', 'name', 'open', 'pardir', 'path', 'pathsep', 'pipe', 'popen', 'popen2', 'popen3', 'popen4', 'putenv', 'read', 'remove', 'removedirs', 'rename', 'renames', 'rmdir', 'sep', 'spawnl', 'spawnle', 'spawnv', 'spawnve', 'startfile', 'stat', 'stat_float_times', 'stat_result', 'statvfs_result', 'strerror', 'sys', 'system', 'tempnam', 'times', 'tmpfile', 'tmpnam', 'umask', 'unlink', 'unsetenv', 'urandom', 'utime', 'waitpid', 'walk', 'write']
>>> from os import getcwd, listdir, getcwd
>>> os.mkdir()

Traceback (most recent call last):
  File "<pyshell#252>", line 1, in <module>
    os.mkdir()
TypeError: mkdir() takes at least 1 argument (0 given)
>>> os.mkdir('day6')
>>> os.chdir('day6')
>>> os.remove('filenametoremove')

Traceback (most recent call last):
  File "<pyshell#255>", line 1, in <module>
    os.remove('filenametoremove')
WindowsError: [Error 2] The system cannot find the file specified: 'filenametoremove'
>>> os.system(dir)

Traceback (most recent call last):
  File "<pyshell#256>", line 1, in <module>
    os.system(dir)
TypeError: must be string, not builtin_function_or_method
>>> os.system('dir')
0
>>> command = os.popen('dir')
>>> print command.read()
 Volume in drive C has no label.
 Volume Serial Number is AECD-833C

 Directory of C:\Python27\day6

10/07/2016  11:42 AM    <DIR>          .
10/07/2016  11:42 AM    <DIR>          ..
               0 File(s)              0 bytes
               2 Dir(s)   3,546,099,712 bytes free

>>> os.stat('C:\Python27\day6')
nt.stat_result(st_mode=16895, st_ino=0L, st_dev=0, st_nlink=0, st_uid=0, st_gid=0, st_size=0L, st_atime=1468131128L, st_mtime=1468131128L, st_ctime=1468131128L)
>>> dir(os.path)
['__all__', '__builtins__', '__doc__', '__file__', '__name__', '__package__', '_getfullpathname', 'abspath', 'altsep', 'basename', 'commonprefix', 'curdir', 'defpath', 'devnull', 'dirname', 'exists', 'expanduser', 'expandvars', 'extsep', 'genericpath', 'getatime', 'getctime', 'getmtime', 'getsize', 'isabs', 'isdir', 'isfile', 'islink', 'ismount', 'join', 'lexists', 'normcase', 'normpath', 'os', 'pardir', 'pathsep', 'realpath', 'relpath', 'sep', 'split', 'splitdrive', 'splitext', 'splitunc', 'stat', 'supports_unicode_filenames', 'sys', 'walk', 'warnings']
>>> os.path.getsize()

Traceback (most recent call last):
  File "<pyshell#262>", line 1, in <module>
    os.path.getsize()
TypeError: getsize() takes exactly 1 argument (0 given)
>>> os.path.getsize('C:\Python27\day6\empty.txt')
0L
>>> dir(os.stat)
['__call__', '__class__', '__cmp__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__self__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
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
    __all__ = ['abspath', 'altsep', 'basename', 'commonprefix', 'curdir', ...
    altsep = '/'
    curdir = '.'
    defpath = r'.;C:\bin'
    devnull = 'nul'
    extsep = '.'
    pardir = '..'
    pathsep = ';'
    sep = r'\'
    supports_unicode_filenames = True


>>> ================================ RESTART ================================
>>> 
Please enter dir name :.

Traceback (most recent call last):
  File "D:/Jatin Sir Python Training/remove_emptyfile.py", line 4, in <module>
    os.chdir('dir_name')
WindowsError: [Error 2] The system cannot find the file specified: 'dir_name'
>>> ================================ RESTART ================================
>>> 
Please enter dir name :.
>>> ================================ RESTART ================================
>>> 
['D:/Jatin Sir Python Training/sys_argument.py']
Your first argument is 

Traceback (most recent call last):
  File "D:/Jatin Sir Python Training/sys_argument.py", line 3, in <module>
    print 'Your first argument is ', sys.argv[1]
IndexError: list index out of range
>>> ================================ RESTART ================================
>>> 
['D:/Jatin Sir Python Training/sys_argument.py']
Your first argument is 

Traceback (most recent call last):
  File "D:/Jatin Sir Python Training/sys_argument.py", line 3, in <module>
    print "Your first argument is ", sys.argv[1]
IndexError: list index out of range
>>> import time
>>> start = time.time()
>>> start
1468134769.543
>>> # hiphop time ... i.e. from 1971 it shows no. of seconds
>>> time.sleep(10)
>>> # delay/sleeps for 10 seconds
>>> import time
>>> dir(time)
['__doc__', '__name__', '__package__', 'accept2dyear', 'altzone', 'asctime', 'clock', 'ctime', 'daylight', 'gmtime', 'localtime', 'mktime', 'sleep', 'strftime', 'strptime', 'struct_time', 'time', 'timezone', 'tzname']
>>> help(time.localtime)
Help on built-in function localtime in module time:

localtime(...)
    localtime([seconds]) -> (tm_year,tm_mon,tm_mday,tm_hour,tm_min,
                              tm_sec,tm_wday,tm_yday,tm_isdst)
    
    Convert seconds since the Epoch to a time tuple expressing local time.
    When 'seconds' is not passed in, convert the current time instead.

>>> print time.localtime
<built-in function localtime>
>>> print time.localtime()
time.struct_time(tm_year=2016, tm_mon=7, tm_mday=10, tm_hour=12, tm_min=46, tm_sec=11, tm_wday=6, tm_yday=192, tm_isdst=0)
>>> print time.localtime()[1]
7
>>> print time.localtime()[2]
10
>>> # print fetching localtime.tm_mon, locatime.tm_hour..
>>> time.timezone
-19800
>>> time.tzname
('India Standard Time', 'India Daylight Time')
>>> help(time.daytime)

Traceback (most recent call last):
  File "<pyshell#282>", line 1, in <module>
    help(time.daytime)
AttributeError: 'module' object has no attribute 'daytime'
>>> help(time.date)

Traceback (most recent call last):
  File "<pyshell#283>", line 1, in <module>
    help(time.date)
AttributeError: 'module' object has no attribute 'date'
>>> help(time)
Help on built-in module time:

NAME
    time - This module provides various functions to manipulate time values.

FILE
    (built-in)

DESCRIPTION
    There are two standard representations of time.  One is the number
    of seconds since the Epoch, in UTC (a.k.a. GMT).  It may be an integer
    or a floating point number (to represent fractions of seconds).
    The Epoch is system-defined; on Unix, it is generally January 1st, 1970.
    The actual value can be retrieved by calling gmtime(0).
    
    The other representation is a tuple of 9 integers giving local time.
    The tuple items are:
      year (four digits, e.g. 1998)
      month (1-12)
      day (1-31)
      hours (0-23)
      minutes (0-59)
      seconds (0-59)
      weekday (0-6, Monday is 0)
      Julian day (day in the year, 1-366)
      DST (Daylight Savings Time) flag (-1, 0 or 1)
    If the DST flag is 0, the time is given in the regular time zone;
    if it is 1, the time is given in the DST time zone;
    if it is -1, mktime() should guess based on the date and time.
    
    Variables:
    
    timezone -- difference in seconds between UTC and local standard time
    altzone -- difference in  seconds between UTC and local DST time
    daylight -- whether local time should reflect DST
    tzname -- tuple of (standard time zone name, DST time zone name)
    
    Functions:
    
    time() -- return current time in seconds since the Epoch as a float
    clock() -- return CPU time since process start as a float
    sleep() -- delay for a number of seconds given as a float
    gmtime() -- convert seconds since Epoch to UTC tuple
    localtime() -- convert seconds since Epoch to local time tuple
    asctime() -- convert time tuple to string
    ctime() -- convert time in seconds to string
    mktime() -- convert local time tuple to seconds since Epoch
    strftime() -- convert time tuple to string according to format specification
    strptime() -- parse string to time tuple according to format specification
    tzset() -- change the local timezone

CLASSES
    __builtin__.object
        struct_time
    
    class struct_time(__builtin__.object)
     |  The time value as returned by gmtime(), localtime(), and strptime(), and
     |  accepted by asctime(), mktime() and strftime().  May be considered as a
     |  sequence of 9 integers.
     |  
     |  Note that several fields' values are not the same as those defined by
     |  the C language standard for struct tm.  For example, the value of the
     |  field tm_year is the actual year, not year - 1900.  See individual
     |  fields' descriptions for details.
     |  
     |  Methods defined here:
     |  
     |  __add__(...)
     |      x.__add__(y) <==> x+y
     |  
     |  __contains__(...)
     |      x.__contains__(y) <==> y in x
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getitem__(...)
     |      x.__getitem__(y) <==> x[y]
     |  
     |  __getslice__(...)
     |      x.__getslice__(i, j) <==> x[i:j]
     |      
     |      Use of negative indices is not supported.
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __len__(...)
     |      x.__len__() <==> len(x)
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __mul__(...)
     |      x.__mul__(n) <==> x*n
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __reduce__(...)
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __rmul__(...)
     |      x.__rmul__(n) <==> n*x
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  tm_hour
     |      hours, range [0, 23]
     |  
     |  tm_isdst
     |      1 if summer time is in effect, 0 if not, and -1 if unknown
     |  
     |  tm_mday
     |      day of month, range [1, 31]
     |  
     |  tm_min
     |      minutes, range [0, 59]
     |  
     |  tm_mon
     |      month of year, range [1, 12]
     |  
     |  tm_sec
     |      seconds, range [0, 61])
     |  
     |  tm_wday
     |      day of week, range [0, 6], Monday is 0
     |  
     |  tm_yday
     |      day of year, range [1, 366]
     |  
     |  tm_year
     |      year, for example, 1993
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  __new__ = <built-in method __new__ of type object>
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
     |  
     |  n_fields = 9
     |  
     |  n_sequence_fields = 9
     |  
     |  n_unnamed_fields = 0

FUNCTIONS
    asctime(...)
        asctime([tuple]) -> string
        
        Convert a time tuple to a string, e.g. 'Sat Jun 06 16:26:11 1998'.
        When the time tuple is not present, current time as returned by localtime()
        is used.
    
    clock(...)
        clock() -> floating point number
        
        Return the CPU time or real time since the start of the process or since
        the first call to clock().  This has as much precision as the system
        records.
    
    ctime(...)
        ctime(seconds) -> string
        
        Convert a time in seconds since the Epoch to a string in local time.
        This is equivalent to asctime(localtime(seconds)). When the time tuple is
        not present, current time as returned by localtime() is used.
    
    gmtime(...)
        gmtime([seconds]) -> (tm_year, tm_mon, tm_mday, tm_hour, tm_min,
                               tm_sec, tm_wday, tm_yday, tm_isdst)
        
        Convert seconds since the Epoch to a time tuple expressing UTC (a.k.a.
        GMT).  When 'seconds' is not passed in, convert the current time instead.
    
    localtime(...)
        localtime([seconds]) -> (tm_year,tm_mon,tm_mday,tm_hour,tm_min,
                                  tm_sec,tm_wday,tm_yday,tm_isdst)
        
        Convert seconds since the Epoch to a time tuple expressing local time.
        When 'seconds' is not passed in, convert the current time instead.
    
    mktime(...)
        mktime(tuple) -> floating point number
        
        Convert a time tuple in local time to seconds since the Epoch.
    
    sleep(...)
        sleep(seconds)
        
        Delay execution for a given number of seconds.  The argument may be
        a floating point number for subsecond precision.
    
    strftime(...)
        strftime(format[, tuple]) -> string
        
        Convert a time tuple to a string according to a format specification.
        See the library reference manual for formatting codes. When the time tuple
        is not present, current time as returned by localtime() is used.
    
    strptime(...)
        strptime(string, format) -> struct_time
        
        Parse a string to a time tuple according to a format specification.
        See the library reference manual for formatting codes (same as strftime()).
    
    time(...)
        time() -> floating point number
        
        Return the current time in seconds since the Epoch.
        Fractions of a second may be present if the system clock provides them.

DATA
    accept2dyear = 1
    altzone = -23400
    daylight = 0
    timezone = -19800
    tzname = ('India Standard Time', 'India Daylight Time')


>>> dir(time)
['__doc__', '__name__', '__package__', 'accept2dyear', 'altzone', 'asctime', 'clock', 'ctime', 'daylight', 'gmtime', 'localtime', 'mktime', 'sleep', 'strftime', 'strptime', 'struct_time', 'time', 'timezone', 'tzname']
>>> time.clock
<built-in function clock>
>>> time.clock()
2.5657626344566527e-06
>>> import daytime

Traceback (most recent call last):
  File "<pyshell#288>", line 1, in <module>
    import daytime
ImportError: No module named daytime
>>> import datetime
>>> datetime
<module 'datetime' (built-in)>
>>> datetime()

Traceback (most recent call last):
  File "<pyshell#291>", line 1, in <module>
    datetime()
TypeError: 'module' object is not callable
>>> dir(datetime)
['MAXYEAR', 'MINYEAR', '__doc__', '__name__', '__package__', 'date', 'datetime', 'datetime_CAPI', 'time', 'timedelta', 'tzinfo']
>>> datetime.time
<type 'datetime.time'>
>>> datetime.time()
datetime.time(0, 0)
>>> datetime.datetime()

Traceback (most recent call last):
  File "<pyshell#295>", line 1, in <module>
    datetime.datetime()
TypeError: Required argument 'year' (pos 1) not found
>>> datetime.datetime(today)

Traceback (most recent call last):
  File "<pyshell#296>", line 1, in <module>
    datetime.datetime(today)
NameError: name 'today' is not defined
>>> datetime.datetime()

Traceback (most recent call last):
  File "<pyshell#297>", line 1, in <module>
    datetime.datetime()
TypeError: Required argument 'year' (pos 1) not found
>>> datetime.datetime
<type 'datetime.datetime'>
>>> help(datetime.datetime)
Help on class datetime in module datetime:

class datetime(date)
 |  datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]])
 |  
 |  The year, month and day arguments are required. tzinfo may be None, or an
 |  instance of a tzinfo subclass. The remaining arguments may be ints or longs.
 |  
 |  Method resolution order:
 |      datetime
 |      date
 |      __builtin__.object
 |  
 |  Methods defined here:
 |  
 |  __add__(...)
 |      x.__add__(y) <==> x+y
 |  
 |  __eq__(...)
 |      x.__eq__(y) <==> x==y
 |  
 |  __ge__(...)
 |      x.__ge__(y) <==> x>=y
 |  
 |  __getattribute__(...)
 |      x.__getattribute__('name') <==> x.name
 |  
 |  __gt__(...)
 |      x.__gt__(y) <==> x>y
 |  
 |  __hash__(...)
 |      x.__hash__() <==> hash(x)
 |  
 |  __le__(...)
 |      x.__le__(y) <==> x<=y
 |  
 |  __lt__(...)
 |      x.__lt__(y) <==> x<y
 |  
 |  __ne__(...)
 |      x.__ne__(y) <==> x!=y
 |  
 |  __radd__(...)
 |      x.__radd__(y) <==> y+x
 |  
 |  __reduce__(...)
 |      __reduce__() -> (cls, state)
 |  
 |  __repr__(...)
 |      x.__repr__() <==> repr(x)
 |  
 |  __rsub__(...)
 |      x.__rsub__(y) <==> y-x
 |  
 |  __str__(...)
 |      x.__str__() <==> str(x)
 |  
 |  __sub__(...)
 |      x.__sub__(y) <==> x-y
 |  
 |  astimezone(...)
 |      tz -> convert to local time in new timezone tz
 |  
 |  ctime(...)
 |      Return ctime() style string.
 |  
 |  date(...)
 |      Return date object with same year, month and day.
 |  
 |  dst(...)
 |      Return self.tzinfo.dst(self).
 |  
 |  isoformat(...)
 |      [sep] -> string in ISO 8601 format, YYYY-MM-DDTHH:MM:SS[.mmmmmm][+HH:MM].
 |      
 |      sep is used to separate the year from the time, and defaults to 'T'.
 |  
 |  replace(...)
 |      Return datetime with new specified fields.
 |  
 |  time(...)
 |      Return time object with same time but with tzinfo=None.
 |  
 |  timetuple(...)
 |      Return time tuple, compatible with time.localtime().
 |  
 |  timetz(...)
 |      Return time object with same time and tzinfo.
 |  
 |  tzname(...)
 |      Return self.tzinfo.tzname(self).
 |  
 |  utcoffset(...)
 |      Return self.tzinfo.utcoffset(self).
 |  
 |  utctimetuple(...)
 |      Return UTC time tuple, compatible with time.localtime().
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  hour
 |  
 |  microsecond
 |  
 |  minute
 |  
 |  second
 |  
 |  tzinfo
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __new__ = <built-in method __new__ of type object>
 |      T.__new__(S, ...) -> a new object with type S, a subtype of T
 |  
 |  combine = <built-in method combine of type object>
 |      date, time -> datetime with same date and time fields
 |  
 |  fromtimestamp = <built-in method fromtimestamp of type object>
 |      timestamp[, tz] -> tz's local time from POSIX timestamp.
 |  
 |  max = datetime.datetime(9999, 12, 31, 23, 59, 59, 999999)
 |  
 |  min = datetime.datetime(1, 1, 1, 0, 0)
 |  
 |  now = <built-in method now of type object>
 |      [tz] -> new datetime with tz's local day and time.
 |  
 |  resolution = datetime.timedelta(0, 0, 1)
 |  
 |  strptime = <built-in method strptime of type object>
 |      string, format -> new datetime parsed from a string (like time.strptime()).
 |  
 |  utcfromtimestamp = <built-in method utcfromtimestamp of type object>
 |      timestamp -> UTC datetime from a POSIX timestamp (like time.time()).
 |  
 |  utcnow = <built-in method utcnow of type object>
 |      Return a new datetime representing UTC day and time.
 |  
 |  ----------------------------------------------------------------------
 |  Methods inherited from date:
 |  
 |  __format__(...)
 |      Formats self with strftime.
 |  
 |  isocalendar(...)
 |      Return a 3-tuple containing ISO year, week number, and weekday.
 |  
 |  isoweekday(...)
 |      Return the day of the week represented by the date.
 |      Monday == 1 ... Sunday == 7
 |  
 |  strftime(...)
 |      format -> strftime() style string.
 |  
 |  toordinal(...)
 |      Return proleptic Gregorian ordinal.  January 1 of year 1 is day 1.
 |  
 |  weekday(...)
 |      Return the day of the week represented by the date.
 |      Monday == 0 ... Sunday == 6
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from date:
 |  
 |  day
 |  
 |  month
 |  
 |  year
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes inherited from date:
 |  
 |  fromordinal = <built-in method fromordinal of type object>
 |      int -> date corresponding to a proleptic Gregorian ordinal.
 |  
 |  today = <built-in method today of type object>
 |      Current date or datetime:  same as self.__class__.fromtimestamp(time.time()).

>>> datetime.datetime.today
<built-in method today of type object at 0x1E210670>
>>> datetime.datetime.today()
datetime.datetime(2016, 7, 10, 12, 52, 31, 190000)
>>> print datetime.datetime.now()
2016-07-10 12:52:45.308000
>>> print datetime.datetime.today()
2016-07-10 12:52:54.637000
>>> now = datetime.datetime.now()
>>> olddate = datetime.datetime(2016, 1,1)
>>> print olddate
2016-01-01 00:00:00
>>> print now
2016-07-10 12:53:22.187000
>>> print now - olddate
191 days, 12:53:22.187000
>>> datetime.timedelta(2)
datetime.timedelta(2)
>>> after_two_days = datetime.timedelta(2)
>>> now + after_two_days
datetime.datetime(2016, 7, 12, 12, 53, 22, 187000)
>>> after_two_days_date = now + after_two_days
>>> print after_two_days_date
2016-07-12 12:53:22.187000
>>> #*** The module always load once in a program / in namespace. For next time you have to reimport
>>> # in case of reloading of module
>>> reload(modulename)

Traceback (most recent call last):
  File "<pyshell#316>", line 1, in <module>
    reload(modulename)
NameError: name 'modulename' is not defined
>>> # modules will import by checking below sequence
>>> # 1) built-in-functions
>>> # 2) current location
>>> # 3) PYTHONPATH
>>> # 4) Installation dir of python i.e. C:/Python/2.7/lib
>>> print sys.path
['D:/Jatin Sir Python Training', 'C:\\Python27\\Lib\\idlelib', 'C:\\Windows\\system32\\python27.zip', 'C:\\Python27\\DLLs', 'C:\\Python27\\lib', 'C:\\Python27\\lib\\plat-win', 'C:\\Python27\\lib\\lib-tk', 'C:\\Python27', 'C:\\Python27\\lib\\site-packages']
>>> 
>>> 
>>> 
>>> 
>>> 

>>> dir(open)
['__call__', '__class__', '__cmp__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__self__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
>>> dir(file)
['__class__', '__delattr__', '__doc__', '__enter__', '__exit__', '__format__', '__getattribute__', '__hash__', '__init__', '__iter__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'close', 'closed', 'encoding', 'errors', 'fileno', 'flush', 'isatty', 'mode', 'name', 'newlines', 'next', 'read', 'readinto', 'readline', 'readlines', 'seek', 'softspace', 'tell', 'truncate', 'write', 'writelines', 'xreadlines']
>>> open.
SyntaxError: invalid syntax
>>> help(open.__call__)
Help on method-wrapper object:

__call__ = class method-wrapper(object)
 |  Methods defined here:
 |  
 |  __call__(...)
 |      x.__call__(...) <==> x(...)
 |  
 |  __cmp__(...)
 |      x.__cmp__(y) <==> cmp(x,y)
 |  
 |  __getattribute__(...)
 |      x.__getattribute__('name') <==> x.name
 |  
 |  __hash__(...)
 |      x.__hash__() <==> hash(x)
 |  
 |  __repr__(...)
 |      x.__repr__() <==> repr(x)
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __objclass__
 |  
 |  __self__

>>> 
				    
>>> dir(file)
['__class__', '__delattr__', '__doc__', '__enter__', '__exit__', '__format__', '__getattribute__', '__hash__', '__init__', '__iter__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'close', 'closed', 'encoding', 'errors', 'fileno', 'flush', 'isatty', 'mode', 'name', 'newlines', 'next', 'read', 'readinto', 'readline', 'readlines', 'seek', 'softspace', 'tell', 'truncate', 'write', 'writelines', 'xreadlines']
>>> help(exists)

Traceback (most recent call last):
  File "<pyshell#334>", line 1, in <module>
    help(exists)
NameError: name 'exists' is not defined
>>> 
