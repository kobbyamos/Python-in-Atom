'''# Since all are false, false is returned
print (any([False, False, False, False]))

# Here the method will short-circuit at the
# second item (True) and will return True.
print (any([False, True, False, False]))

# Here the method will short-circuit at the
# first (True) and will return True.
print (any([True, False, False, False]))'''

# importing operator module
import operator

# Initializing variables
a = 3
b = 3

# using add() to add two numbers
'''print ("The addition of numbers is :",end="");
print (operator.add(a, b))

# using sub() to subtract two numbers
print ("The difference of numbers is :",operator.sub(a,b));
print ("The difference of numbers is : ",end="");
print (operator.sub(a, b))

# using mul() to multiply two numbers
print ("The product of numbers is :",end="");
print (operator.mul(a, b))

print ("The true division of numbers is : ",end="");
print (operator.truediv(a,b))

# using floordiv() to divide two numbers
print ("The floor division of numbers is : ",end="");
print (operator.floordiv(a,b))

# using pow() to exponentiate two numbers
print ("The exponentiation of numbers is : ",end="");
print (operator.pow(a,b))

# using mod() to take modulus of two numbers
print ("The modulus of numbers is : ",end="");
print (operator.mod(a,b))'''

# using lt() to check if a is less than b
if(operator.lt(a,b)):
       print ("3 is less than 3")
else : print ("3 is not less than 3")

# using le() to check if a is less than or equal to b
if(operator.le(a,b)):
       print ("3 is less than or equal to 3")
else : print ("3 is not less than or equal to 3")

# using eq() to check if a is equal to b
if (operator.eq(a,b)):
       print ("3 is equal to 3")
else : print ("3 is not equal to 3")

# using gt() to check if a is greater than b
if (operator.gt(a,b)):
       print ("4 is greater than 3")
else : print ("4 is not greater than 3")

# using ge() to check if a is greater than or equal to b
if (operator.ge(a,b)):
       print ("4 is greater than or equal to 3")
else : print ("4 is not greater than or equal to 3")

# using ne() to check if a is not equal to b
if (operator.ne(a,b)):
       print ("4 is not equal to 3")
else : print ("4 is equal to 3")
