'''a = "This is a string"
print (a)

# Declaring a list
L = [1, "a" , "string" , 1+2]
print (L)
L.append(6)
print (L)
L.pop()
print (L)
print (L[1])

#tuple is immutable
tup = (1, "a", "string", 1+2)
print(tup)
print(tup[3])

i = 1
while (i < 2):
    print(i)
    i += 1
    print()

s = "Hello World"
for i in s :
    print (i)

for i in range(0, 10):
    print (i)


# Creating a String
# with single Quotes
String1 = 'Welcome to the Geeks World'
print("String with the use of Single Quotes: ")
print(String1)

# Creating a String
# with double Quotes
String1 = "I'm a Geek"
print("\nString with the use of Double Quotes: ")
print(String1)'''


# Creating String with triple
# Quotes allows multiple lines
#String1 = '''Geeks
#            For
#            Life'''
#print("\nCreating a multiline String: ")
#print(String1)

'''
String1 = "GeeksForGeeks"
print("Initial String: ")
print(String1)

# Printing First character
print("\nFirst character of String is: ")
print(String1[0])

# Printing Last character
print("\nLast character of String is: ")
print(String1[-1])

# Creating a String
String1 = "GeeksForGeeks"
print("Initial String: ")
print(String1)

# Printing 3rd to 12th character
print("\nSlicing characters from 3-12: ")
print(String1[3:12])

# Printing characters between
# 3rd and 2nd last character
print("\nSlicing characters between " +
    "3rd and 2nd last character: ")
print(String1[3:-2])
#del(String1) #deleting string
print(String1)


'''
# Escaping Single Quote
#String1 = 'I\'m a "Geek"'
#print("\nEscaping Single Quote: ")
#print(String1)

# Escaping Double Quotes
#String1 = "I'm a \"Geek\""
#print("\nEscaping Double Quotes: ")
#print(String1)

# Printing Paths with the
# use of Escape Sequences
#string2="C:\\Python\\Geeks\\"
#print("\nEscaping Backslashes: ")
#print(string2)
'''
string3="{} {} {}".format('Geeks','For','Life')
print("\nPrint String in default order: ")
print(string3)

# Positional Formatting
string3="{1} {0} {2}".format('Geeks','For','Life')
print("\nPrint String in Positional order: ")
print(string3)

# Keyword Formatting
string3 = "{l} {f} {g}".format(g='Geeks', f='For', l='Life')
print("\nPrint String in order of Keywords: ")
print(string3)

# Formatting of Integers
String1 = "{0:b}".format(16)
print("\nBinary representation of 16 is ")
print(String1)

# Formatting of Floats
String1 = "{0:e}".format(165.6458)
print("\nExponent representation of 165.6458 is ")
print(String1)

# Rounding off Integers
String1 = "{0:.2f}".format(1/6)
print("\none-sixth is : ")
print(String1)'''

# String alignment
String1 = "|{:<10}|{:^10}|{:>10}|".format('Geeks', 'for', 'Geeks')
print("\nLeft, center and right alignment with Formatting: ")
print(String1)

# To demonstrate aligning of spaces
String1 = "\n{0:^16} was founded in {1:<4}!".format("GeeksforGeeks", 2009)
print(String1)

Integer1 = 12.3456789
print("Formatting in 3.2f format: ")
print('The value of Integer1 is %3.2f' % Integer1)
print("\nFormatting in 3.4f format: ")
print('The value of Integer1 is %3.4f' % Integer1)
