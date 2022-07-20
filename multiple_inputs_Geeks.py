"""
num1 = float(input("Enter your value: "))
num2 = int (input("Enter your value: "))
print("The total of ", num1, "and", num2, "is", num1 + num2)


#multiple comments
x, y = input("Enter two values: ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)
print()

# taking two inputs at a time
a, b = input("Enter your full name: ").split()
print("First name is {} and surname is {}".format(a, b))
print()

a = input ("Enter your given name: ")
b = input ("Enter your surname name: ")
print("Your given name is" ,a, "and your surname is",b, ".")
print("Your given name is {} and your surname is {}".format(a, b))


# taking multiple inputs at a time
# and type casting using list() function
x = list(map(str, input("Enter the names of the students: ").split()))
print("List of students: ", x)


# taking three input at a time
x, y, z = [int(x) for x in input("Enter three values: ").split()]
print("First Number is: ", x)
print("Second Number is: ", y)
print("Third Number is: ", z)"""
print()

# taking three input at a time and inputs separated by commas
x, y, z = [str(x) for x in input("Enter your full name: ").split(",")]
print("First name is: ", x)
print("Middle name is: ", y)
print("surname Number is: ", z)
print("Your first name is {}\n Your middle name is {}\n and your surname is {}".format(x,y,z))
