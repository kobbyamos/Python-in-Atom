'''# Python program to demonstrate Keyword Arguments
def student(firstname, lastname):
	print(firstname, lastname)


# Keyword arguments
student(firstname='Geeks', lastname='Practice')
student(lastname='Practice', firstname='Geeks')

def myFun(*argv):
    for x in argv:
        print (x)

myFun("Hello", 'Welcome', 'to', 'GeeksforGeeks')


# Python program to illustrate
# *kwargs for variable number of keyword arguments


def myFun(**kwargs):
	for key, value in kwargs.items():
		print("%s == %s" % (key, value))


# Driver code
myFun(fir1st='Geeks', mid='for', last='Geeks')

# A simple Python function to check
# whether x is even or odd


def evenOdd(x):
	"""Function to check if the number is even or odd"""

	if (x % 2 == 0):
		print("even")
	else:
		print("odd")


# Driver code to call the function
print(evenOdd.__doc__)
#print(evenOdd(2))
evenOdd(3)

def square_value(num):
	"""This function returns the square value of the entered number"""
	return num**2


print(square_value(2))
print(square_value(-4))
print(square_value.__doc__)

# Here x is a new reference to same list lst
def myFun(x):
	x[0] = 20


# Driver Code (Note that lst is modified
# after function call.

lst = [10, 11, 12, 13, 14, 15]
print(lst)
myFun(lst)
print(lst)

# Python program to
# demonstrate accessing of
# variables of nested functions

def f1():
	s = 'I love GeeksforGeeks'

	def f2():
		print(s)

	f2()

# Driver's code
f1()
f2()

# Python program to illustrate cube of a number
# showing difference between def() and lambda().


def cube(y):
	return y*y*y;

g = lambda x: x*x*x
print(g(7))

print(cube(5))

a = [100, 2, 8, 60, 5, 4, 3, 31, 10, 11]

# in filter either we use assignment or
# conditional operator, the pass actual
# parameter will get return
filtered = filter (lambda x: x % 2 == 0, a)
print(list(filtered))

# in map either we use assignment or
# conditional operator, the result of
# the value will get returned
mapped = map (lambda x: x % 2 == 0, a)
print(list(mapped))

def f():
	# local variable
	s = "I love Geeksforgeeks"
	print("Inside Function:", s)

# Driver code
a = "I Geeksforgeeks"
#f()
print(a)

# Python program showing to modify
# a global value without using global
# keyword

a = 15

# function to change a global value
def change():
	a=45
	# increment value of a by 5
	a = a + 5
	print(a)

change()
print(a)

import config
import modify
print(config.x)
print(config.y)
print(config.z)

# Python program to illustrate functions
# can be treated as objects
def shout(text):
	return text.upper()

print (shout('Hello'))

yell = shout

print (yell('Hello'))

# Python program to illustrate functions
# can be passed as arguments to other functions
def shout(text):
	return text.upper()

def whisper(text):
	return text.lower()

def greet(func):
	# storing the function in a variable
	greeting = func("""Hi, I am created by a function passed as an argument.""")
	print (greeting)

greet(shout)
greet(whisper)'''

# Python program to illustrate functions
# Functions can return another function

def create_adder(x):
	def adder(y):
		return x+y

	return adder

add_15 = create_adder(15)

print (add_15(10))
