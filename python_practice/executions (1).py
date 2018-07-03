Python 2.7.9 (default, Dec 10 2014, 12:24:55) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> a = 10
>>> b = 3
>>> a + b
13
>>> print a + b
13
>>> a * b
30
>>> a - b
7
>>> a / b
3
>>> 10.0/3
3.3333333333333335
>>> 10/3.0
3.3333333333333335
>>> 10./3
3.3333333333333335
>>> 10/3.
3.3333333333333335
>>> a
10
>>> float(10)
10.0
>>> int(10.1)
10
>>> 
>>> 10 ** 2
100
>>> 10 % 2
0
>>> (10 ** 2) * 2 # operartor
200
>>> #PEDMAS
>>> 10 + 2 * 6 - 6 # 10 + 12 - 6
16
>>> 10 + ((2 * 6) - 6) # 10 + 12 - 6
16
>>> 10 * 2 / 4 # operator associativity
5
>>> 10 * (2 / 4) # operator associativity
0
>>> # bit wise operation
>>> 
>>> bin(10)
'0b1010'
>>> 
>>> a = '1000'
>>> int(a)
1000
>>> a = 'Jatin'
>>> int(a)

Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    int(a)
ValueError: invalid literal for int() with base 10: 'Jatin'
>>> bin(10)
'0b1010'
>>> bin(7)
'0b111'
>>> 
>>> bin(-7)
'-0b111'
>>> 
>>> 10 & 7
2
>>> 15 | 16
31
>>> 15 ^ 17
30
>>> int(1010,2)

Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    int(1010,2)
TypeError: int() can't convert non-string with explicit base
>>> int('1010',2)
10
>>> 10 << 2
40
>>> 21 >> 2
5
>>> 
>>> a= 10
>>> a == 10 # True or False
True
>>> a > 2 # True
True
>>> a >= 2
True
>>> if a == 2:
	print 0

	
>>> if a > 2 : print 0

0
>>> 
>>> a < 2
False
>>> a <= 2
False
>>> a != 2
True
>>> a <> 2
True
>>> 
>>> a
10
>>> a is 10 #True
True
>>> a is not 10
False
>>> 
>>> a = 300
>>> a is 300 #?
False
>>> a = 1000
>>> a is 1000
False
>>> a = 250
>>> a is 250
True
>>> name = 'Jatin'
>>> print name + ' Miglani'
Jatin Miglani
>>> name + 10

Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    name + 10
TypeError: cannot concatenate 'str' and 'int' objects
>>> name + str(10)
'Jatin10'
>>> name + ' ' + str(10)
'Jatin 10'
>>> name + ' ' + repr(10)
'Jatin 10'
>>> name + ' ' + `10`
'Jatin 10'
>>> # backtick #inverted commans
>>> 

>>> name
'Jatin'
>>> name + `Miglani`

Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    name + `Miglani`
NameError: name 'Miglani' is not defined
>>> Miglani = 'Miglani'
>>> name + `Miglani`
"Jatin'Miglani'"
>>> 
>>> name + ' ' + 'Miglani'
'Jatin Miglani'
>>> 
>>> 
>>> name
'Jatin'
>>> 
>>> name[0]
'J'
>>> name[4]
'n'
>>> name[5]

Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    name[5]
IndexError: string index out of range
>>> name[-1]
'n'
>>> name[-5]
'J'
>>> name[0] = 'Y'

Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    name[0] = 'Y'
TypeError: 'str' object does not support item assignment
>>> #immutable and mutable property of an object
>>> 
>>> name = 'Yatin'
>>> name[0] = 'Ja'

Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    name[0] = 'Ja'
TypeError: 'str' object does not support item assignment
>>> 
>>> string = 'This is a string'
>>> string = "This is a string"
>>> paragraph = '''
This is a line number 1
This is a line number 2
This is a line number3
'''
>>> print paragraph

This is a line number 1
This is a line number 2
This is a line number3

>>> string[0]
'T'
>>> string[5]
'i'
>>> # string[START:STOP:STEP]
>>> string[5:7:1]
'is'
>>> #step is an optional 1
>>> string[5:7]
'is'
>>> # start and end are also optional
>>> string[0:]
'This is a string'
>>> len(string)
16
>>> string[:]
'This is a string'
>>> string[:8765432]
'This is a string'
>>> 
>>> string
'This is a string'
>>> string[::-1]
'gnirts a si sihT'
>>> 
>>> 
>>> name = 'nitin'
>>> 
>>> name == name[::-1]
True
>>> 
>>> 
>>> string
'This is a string'
>>> string[len(string)-4:]
'ring'
>>> 
>>> 
>>> string[6:0]
''
>>> string[6:0:-1]
'si sih'
>>> 
>>> string
'This is a string'
>>> string + ' Test'
'This is a string Test'
>>> string * 2
'This is a stringThis is a string'
>>> 
>>> '**' * 10
'********************'
>>> 
>>> print '**' * 10 , '\nHello to Python Class\n', '**' * 10
******************** 
Hello to Python Class
********************
>>> 
>>> name
'nitin'
>>> name == 'nitin'
True
>>> name > 'Nitin' #o/p?
True
>>> #ASCII comparison
>>> 
>>> # A - 65, a - 97
>>> 
>>> 
>>> help(raw_input)
Help on built-in function raw_input in module __builtin__:

raw_input(...)
    raw_input([prompt]) -> string
    
    Read a string from standard input.  The trailing newline is stripped.
    If the user hits EOF (Unix: Ctl-D, Windows: Ctl-Z+Return), raise EOFError.
    On Unix, GNU readline is used if enabled.  The prompt string, if given,
    is printed without a trailing newline before reading.

>>> ================================ RESTART ================================
>>> 
What is your name? Jatin
Hello Mr  Jatin
>>> help(input)
Help on built-in function input in module __builtin__:

input(...)
    input([prompt]) -> value
    
    Equivalent to eval(raw_input(prompt)).

>>> ================================ RESTART ================================
>>> 
What is your name? Jatin
Hello Mr  Jatin
What is your age? 35
so your age is  35
>>> ================================ RESTART ================================
>>> 
What is your name? Jatin
Hello Mr  Jatin
What is your age? myage
so your age is  35
>>> ================================ RESTART ================================
>>> 
What is your name? Jatin
Hello Mr  Jatin
What is your age? 35
so your age is  35
>>> ================================ RESTART ================================
>>> 
What is your name? Jatin
Hello Mr  Jatin
What is your age? 35
so your age is  35
>>> 
>>> names = ['Jatin', 'Divyansh', 'Swara', 'Nitin']
>>> names[0]
'Jatin'
>>> names[4]

Traceback (most recent call last):
  File "<pyshell#157>", line 1, in <module>
    names[4]
IndexError: list index out of range
>>> len(names)
4
>>> names[len(names)-1]
'Nitin'
>>> names[-1]
'Nitin'
>>> names[-4]
'Jatin'
>>> names[0] = 'Yatin'
>>> print names
['Yatin', 'Divyansh', 'Swara', 'Nitin']
>>> 
>>> names = 'This is my name'
>>> names[0]
'T'
>>> names = ['Jatin', 'Divyansh', 'Swara', 'Nitin']
>>> names + names
['Jatin', 'Divyansh', 'Swara', 'Nitin', 'Jatin', 'Divyansh', 'Swara', 'Nitin']
>>> names * 2
['Jatin', 'Divyansh', 'Swara', 'Nitin', 'Jatin', 'Divyansh', 'Swara', 'Nitin']
>>> 
>>> names
['Jatin', 'Divyansh', 'Swara', 'Nitin']
>>> names[3:0]
[]
>>> names[3:0:-1]
['Nitin', 'Swara', 'Divyansh']
>>> 
>>> names[::-1]
['Nitin', 'Swara', 'Divyansh', 'Jatin']
>>> names = names[::-1]
>>> names
['Nitin', 'Swara', 'Divyansh', 'Jatin']
>>> 
>>> lnames = names
>>> lname is names

Traceback (most recent call last):
  File "<pyshell#180>", line 1, in <module>
    lname is names
NameError: name 'lname' is not defined
>>> lnames is names
True
>>> names[0] = 'Yatin'
>>> print
[0]

>>> print lnames
['Yatin', 'Swara', 'Divyansh', 'Jatin']
>>> 
>>> 
>>> llnames = ['Yatin', 'Swara', 'Divyansh', 'Jatin']
>>> names
['Yatin', 'Swara', 'Divyansh', 'Jatin']
>>> lnames
['Yatin', 'Swara', 'Divyansh', 'Jatin']
>>> 
>>> llnames is names
False
>>> lname is names

Traceback (most recent call last):
  File "<pyshell#192>", line 1, in <module>
    lname is names
NameError: name 'lname' is not defined
>>> lnames is names
True
>>> lnames == llnames
True
>>> 
>>> 
