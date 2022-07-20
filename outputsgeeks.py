'''import time
 
count_seconds = 3
for i in reversed(range(count_seconds + 1)):
    if i > 0:
        print(i, end='>>>', flush = True) #Flush makes it sequential in cmd
        time.sleep(1) #seconds to wait or delay in execution
    else:
        print('Start working')

import io
 
# declare a dummy file
dummy_file = io.StringIO()
 
# add message to the dummy file
print('Hello Geeks!!', file=dummy_file)
 
# get the value from dummy file
dummy_file.getvalue()

# code for disabling the softspace feature
print('G', 'F', 'G', sep=' ')

        
# using end argument continues the line with the next sentence
print("Python", end='@')
print("GeeksforGeeks")

print("geeks")
print("geeksforgeeks")

a = [1,2,3,4]
for i in range(4):
     print(a[i], end= " ") #listed in an array horizontal form
     #print(a[i]) #listed in an array vertical form

l=[1,2,3,4,5,6]
 
# using * symbol prints the list
# elements in a single line
#print(l) #Print the list in array separated by commas
print(*l) #Print the list 


# using end argument continues the line with the next sentence
print("Python", end='@')
print("GeeksforGeeks", end=' ')
print (' the best')

print("Geeks : %2d, Portal : %5.4f" % (1000.254, 05.533)) #specifying the string modulo operator

print('{0} and {1}'.format('Geeks', 'Portal')) #using position to index an object
 
print('{1} and {0}'.format('Geeks', 'Portal'))

print(f"I love {'Geeks'} for \"{'Geeks'}!\"")'''

print('Number one portal is {0}, {1}, and {other}.'
     .format('Geeks', 'For', other ='Geeks'))
