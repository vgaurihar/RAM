'''
For input and raw_input functions
'''
print __doc__
#name = raw_input('What is your name: ')
#print 'Hello Mr.', name

#age = input('What is your age: ')
#print 'Your age is ', age


#string = int(raw_input('Pkease enter any string :'))
string = raw_input('Pkease enter any string :')
print 'String is ', string


#a = int(raw_input('What is your name: '))
# I enter name in string and error comes as : 'ValueError: invalid literal for int() with base 10: 'vaibhav''


a = eval(raw_input('What is your name: '))
print 'Hello Mr.', a
# I enter name in string and error comes as : 'NameError: name 'vaibhav' is not defined'


# 'eval' evaluates value of given string / int / etc



