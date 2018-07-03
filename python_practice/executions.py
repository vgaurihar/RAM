Python 2.7.9 (default, Dec 10 2014, 12:24:55) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print 'Hello World!'
Hello World!
>>> print 'Hello World!'
Hello World!
>>> # Comment 1  - Orange color is used for pre-defined/keywords variable
>>> print Hello World
SyntaxError: invalid syntax
>>> print Hello

Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print Hello
NameError: name 'Hello' is not defined
>>> print('Hello World')
Hello World
>>> # in Python3, print is a builtin function
>>> sum([1,2,3])
6
>>> # All purple colors names are builtin functions
>>> help('print')
The "print" statement
*********************

   print_stmt ::= "print" ([expression ("," expression)* [","]]
                  | ">>" expression [("," expression)+ [","]])

"print" evaluates each expression in turn and writes the resulting
object to standard output (see below).  If an object is not a string,
it is first converted to a string using the rules for string
conversions.  The (resulting or original) string is then written.  A
space is written before each object is (converted and) written, unless
the output system believes it is positioned at the beginning of a
line.  This is the case (1) when no characters have yet been written
to standard output, (2) when the last character written to standard
output is a whitespace character except "' '", or (3) when the last
write operation on standard output was not a "print" statement. (In
some cases it may be functional to write an empty string to standard
output for this reason.)

Note: Objects which act like file objects but which are not the
  built-in file objects often do not properly emulate this aspect of
  the file object's behavior, so it is best not to rely on this.

A "'\n'" character is written at the end, unless the "print" statement
ends with a comma.  This is the only action if the statement contains
just the keyword "print".

Standard output is defined as the file object named "stdout" in the
built-in module "sys".  If no such object exists, or if it does not
have a "write()" method, a "RuntimeError" exception is raised.

"print" also has an extended form, defined by the second portion of
the syntax described above. This form is sometimes referred to as
""print" chevron." In this form, the first expression after the ">>"
must evaluate to a "file-like" object, specifically an object that has
a "write()" method as described above.  With this extended form, the
subsequent expressions are printed to this file object.  If the first
expression evaluates to "None", then "sys.stdout" is used as the file
for output.

>>> help('help')

Welcome to Python 2.7!  This is the online help utility.

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at http://docs.python.org/2.7/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, or topics, type "modules",
"keywords", or "topics".  Each module also comes with a one-line summary
of what it does; to list the modules whose summaries contain a given word
such as "spam", type "modules spam".

>>> help()

Welcome to Python 2.7!  This is the online help utility.

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at http://docs.python.org/2.7/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, or topics, type "modules",
"keywords", or "topics".  Each module also comes with a one-line summary
of what it does; to list the modules whose summaries contain a given word
such as "spam", type "modules spam".

help> print
The "print" statement
*********************

   print_stmt ::= "print" ([expression ("," expression)* [","]]
                  | ">>" expression [("," expression)+ [","]])

"print" evaluates each expression in turn and writes the resulting
object to standard output (see below).  If an object is not a string,
it is first converted to a string using the rules for string
conversions.  The (resulting or original) string is then written.  A
space is written before each object is (converted and) written, unless
the output system believes it is positioned at the beginning of a
line.  This is the case (1) when no characters have yet been written
to standard output, (2) when the last character written to standard
output is a whitespace character except "' '", or (3) when the last
write operation on standard output was not a "print" statement. (In
some cases it may be functional to write an empty string to standard
output for this reason.)

Note: Objects which act like file objects but which are not the
  built-in file objects often do not properly emulate this aspect of
  the file object's behavior, so it is best not to rely on this.

A "'\n'" character is written at the end, unless the "print" statement
ends with a comma.  This is the only action if the statement contains
just the keyword "print".

Standard output is defined as the file object named "stdout" in the
built-in module "sys".  If no such object exists, or if it does not
have a "write()" method, a "RuntimeError" exception is raised.

"print" also has an extended form, defined by the second portion of
the syntax described above. This form is sometimes referred to as
""print" chevron." In this form, the first expression after the ">>"
must evaluate to a "file-like" object, specifically an object that has
a "write()" method as described above.  With this extended form, the
subsequent expressions are printed to this file object.  If the first
expression evaluates to "None", then "sys.stdout" is used as the file
for output.

help> for
The "for" statement
*******************

The "for" statement is used to iterate over the elements of a sequence
(such as a string, tuple or list) or other iterable object:

   for_stmt ::= "for" target_list "in" expression_list ":" suite
                ["else" ":" suite]

The expression list is evaluated once; it should yield an iterable
object.  An iterator is created for the result of the
"expression_list".  The suite is then executed once for each item
provided by the iterator, in the order of ascending indices.  Each
item in turn is assigned to the target list using the standard rules
for assignments, and then the suite is executed.  When the items are
exhausted (which is immediately when the sequence is empty), the suite
in the "else" clause, if present, is executed, and the loop
terminates.

A "break" statement executed in the first suite terminates the loop
without executing the "else" clause's suite.  A "continue" statement
executed in the first suite skips the rest of the suite and continues
with the next item, or with the "else" clause if there was no next
item.

The suite may assign to the variable(s) in the target list; this does
not affect the next item assigned to it.

The target list is not deleted when the loop is finished, but if the
sequence is empty, it will not have been assigned to at all by the
loop.  Hint: the built-in function "range()" returns a sequence of
integers suitable to emulate the effect of Pascal's "for i := a to b
do"; e.g., "range(3)" returns the list "[0, 1, 2]".

Note: There is a subtlety when the sequence is being modified by the
  loop (this can only occur for mutable sequences, i.e. lists). An
  internal counter is used to keep track of which item is used next,
  and this is incremented on each iteration.  When this counter has
  reached the length of the sequence the loop terminates.  This means
  that if the suite deletes the current (or a previous) item from the
  sequence, the next item will be skipped (since it gets the index of
  the current item which has already been treated).  Likewise, if the
  suite inserts an item in the sequence before the current item, the
  current item will be treated again the next time through the loop.
  This can lead to nasty bugs that can be avoided by making a
  temporary copy using a slice of the whole sequence, e.g.,

     for x in a[:]:
         if x < 0: a.remove(x)

Related help topics: break, continue, while

help> while
The "while" statement
*********************

The "while" statement is used for repeated execution as long as an
expression is true:

   while_stmt ::= "while" expression ":" suite
                  ["else" ":" suite]

This repeatedly tests the expression and, if it is true, executes the
first suite; if the expression is false (which may be the first time
it is tested) the suite of the "else" clause, if present, is executed
and the loop terminates.

A "break" statement executed in the first suite terminates the loop
without executing the "else" clause's suite.  A "continue" statement
executed in the first suite skips the rest of the suite and goes back
to testing the expression.

Related help topics: break, continue, if, TRUTHVALUE

help> quit

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
>>> 
>>> print 'C:\Users\jatin\Dropbox\Ethans 18th June Batch\Day 1\test'
C:\Users\jatin\Dropbox\Ethans 18th June Batch\Day 1	est
>>> print 'C:\Users\jatin\Dropbox\Ethans 18th June Batch\Day 1\\test'
C:\Users\jatin\Dropbox\Ethans 18th June Batch\Day 1\test
>>> print r'C:\Users\jatin\Dropbox\Ethans 18th June Batch\Day 1\test'
C:\Users\jatin\Dropbox\Ethans 18th June Batch\Day 1\test
>>> execfile(r'C:\Users\jatin\Dropbox\Ethans 18th June Batch\Day 1\hello.py')
Hello World!
>>> help('print')
The "print" statement
*********************

   print_stmt ::= "print" ([expression ("," expression)* [","]]
                  | ">>" expression [("," expression)+ [","]])

"print" evaluates each expression in turn and writes the resulting
object to standard output (see below).  If an object is not a string,
it is first converted to a string using the rules for string
conversions.  The (resulting or original) string is then written.  A
space is written before each object is (converted and) written, unless
the output system believes it is positioned at the beginning of a
line.  This is the case (1) when no characters have yet been written
to standard output, (2) when the last character written to standard
output is a whitespace character except "' '", or (3) when the last
write operation on standard output was not a "print" statement. (In
some cases it may be functional to write an empty string to standard
output for this reason.)

Note: Objects which act like file objects but which are not the
  built-in file objects often do not properly emulate this aspect of
  the file object's behavior, so it is best not to rely on this.

A "'\n'" character is written at the end, unless the "print" statement
ends with a comma.  This is the only action if the statement contains
just the keyword "print".

Standard output is defined as the file object named "stdout" in the
built-in module "sys".  If no such object exists, or if it does not
have a "write()" method, a "RuntimeError" exception is raised.

"print" also has an extended form, defined by the second portion of
the syntax described above. This form is sometimes referred to as
""print" chevron." In this form, the first expression after the ">>"
must evaluate to a "file-like" object, specifically an object that has
a "write()" method as described above.  With this extended form, the
subsequent expressions are printed to this file object.  If the first
expression evaluates to "None", then "sys.stdout" is used as the file
for output.

>>> ================================ RESTART ================================
>>> 
Hello World!

This is the documentation of the program

>>> ================================ RESTART ================================
>>> 
anything
Hello World!
None
>>> 
>>> name = 'Jatin'
>>> $name = 'Jatin'
SyntaxError: invalid syntax
>>> 
>>> 0name = 'Jatin'
SyntaxError: invalid syntax
>>> _name = 'Jatin'
>>> Name0 = 'Jatin'
>>> 
>>> 
>>> if = 10
SyntaxError: invalid syntax
>>> def = 20
SyntaxError: invalid syntax
>>> 
>>> sum = 10
>>> # THis should simply Avoidable
>>> 
>>> sum([1,2,3])

Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    sum([1,2,3])
TypeError: 'int' object is not callable
>>> ================================ RESTART ================================
>>> sum([1,2,3])
6
>>> 
>>> # Object
>>> number = 1
>>> type(number)
<type 'int'>
>>> 
>>> number = 1.1
>>> type(number)
<type 'float'>
>>> 
>>> number = 9876543234567898765432345678987654L
>>> type(number)
<type 'long'>
>>> 
>>> number = 1 + 3j
>>> type(number)
<type 'complex'>
>>> number = 01
>>> type(number)
<type 'int'>
>>> number = x01

Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    number = x01
NameError: name 'x01' is not defined
>>> number = 'x01'
>>> type(number)
<type 'str'>
>>> sum([1,2,3])
6
>>> 
>>> def func():
	'''
        This is the doc of function
        '''
	print 'bla'

	
>>> print func.__doc__

        This is the doc of function
        
>>> 
