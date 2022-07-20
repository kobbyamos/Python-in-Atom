'''a = 9
b = 4

add = a+b
mul = a*b
div1 = a / b

div2 = a // b
mod = a % b
p = a ** b

print(add)

print(mul)
print(div1)
print(div2)
print(mod)
print(p)

print(a > b)
 
# a < b is True
print(a < b)
 
# a == b is False
print(a == b)
 
# a != b is True
print(a != b)
 
# a >= b is False
print(a >= b)
 
# a <= b is True
print(a <= b)

a = True
b = False
 
print(a and b)
print(a or b)
print(not a)
print(not b)


#Membership Operator
x = 24
y = 20
list = [10, 20, 30, 40, 50]
 
if (x not in list):
    print("x is NOT present in given list")
else:
    print("x is present in given list")
 
if (y in list):
    print("y is present in given list")
else:
    print("y is NOT present in given list")


# Examples of Operator Precedence
 
# Precedence of '+' & '*'
expr = 10 + 20 * 30
print(expr)
 
# Precedence of 'or' & 'and' ......."and" has higher precedence over "or"
name = "Alex"
age = 0
 
if name == "Alex" or name == "John" and age >= 2:
    print("Hello! Welcome.")
else:
    print("Good Bye!!")


# Program to demonstrate conditional operator
a, b = 10, 20
 
# Copy value of a in min if a < b else copy b
min = a if a < b else b
max = a if a > b else b
print(min)
print(max)

a, b = 10, 20
 
if a != b:
    if a > b:
        print("a is greater than b")
    else:
        print("b is greater than a")
else:
    print("Both a and b are equal")


a=5
b=7
 
# [statement_on_True] if [condition] else [statement_on_false]
 
print(a,"is greater") if (a>b) else print(b,"is Greater")'''

# Python program to show use of
# + operator for different purposes.
 
print(1 + 2)
 
# concatenate two strings
print("Geeks "+"For")
 
# Product two numbers
print(3 * 4)
 
# Repeat the String
print("Geeks "*4)
