#This code is material from the Programming Hub app.
#All code is typed by Jay Madox Watson as part of lessons within the "Python Certificate" program
#These are my personal reference notes and are not a representation of the product in its entirety

#Section 1: Introduction to Python

#Section 2: Writing our first Program
print("hello world")
    #this is a comment in Python

#Section 3: Storing Data in Python
    #"string" is a sequence of characters
myVar1="hello" #string
    #whole numbers = integers
    #decimal numbers = Float
myVar2=2 #integer
myVar3=25.54 #floating number
input("Enter your name")
name=input("enter your name")
print(name) #String
age=int(input("Enter your age:")) #integer variable
temperature=float(input("Enter the temperature"))  #Float variable   

#Section 4: Calculations in Python 3
    # if adding "2+3", 2 and 3 are "Operands" and +(plus) is called Operator
    # +, -, /, * = arithmetic operators
    # % = Modula Operator
    # // = Truncate Operator
num1=3
num2=5
num3=num1+num2
print("“this means addition is:”, num3")
num1=int.input (4)
num2=int.input (5)
num3=num1+num2
x=4
y=5
print(('x > y is',x>y))
    #logical operators in Python are used for conditional statements that are true or false
    #Operators are AND, OR, and NOT
a=True
b=True
print(('a and b is',a and b))
print(('a or b is',a or b))
print(('not a is',not a))
    #Walrus-operator is another name for assignment expressions
    #using assignment operator 
variable=False 
print(variable)
    #using Walrus operator 
print(variable:=False)

#Section 5: Decision Making
    #if, if-else, elif
    #in Python, Indentation is used to indicate a block of code
if 5==5:
    print("You succesfully learned 'if' statement")
if 5 > 9:print('Oops! Not this time.')

if 5 == 3: 
	print('You successfully learned if statement.') 
else: 
	print('Wow! You also learned about else statement.')	
    #We can check as many conditions as we want to.
if 5==4: 
	print('An if statement. Oh!')
elif 4==4:
	print('That’s something new.')
elif 4>=9: 
	print('Really?')
else:
	print('Not this time')
	
#Section 6: Repeating a task
print('1') 
print('2')
    #Repeating a task
    #What if someone asked you to write the numbers from one to hundred?
print('99')
print('100')
    #2 kinds of loops: For (for variable in sequence: statements)and While (while condition: statements)
for num in range(1,101): print(num)
    #range is a function in Python. range() takes a starting value and an ending value.
range(0,10,2)
    #will return:
[0, 2, 4, 6, 8]
for num in range(1,10,2):
    print(num)
    #What is while Loop?
    #It’s time to explore while loops now.
num = 0
while (num < 10):
	print(num)
	num = num + 1 #update the value of num by 1

#Section 7: Grouping tasks together
    #Functions are a set of instructions which perform a specific task and can be reused multiple times.
    #The specific task can be adding two numbers or finding the greatest number in the list.
    #Functions in Python are written as described below:
    #def functionName (parameters): ----- def is used to declare a function, functionName is the name of the function.
	    #statements
	    #return something
def helloWorld():
    print('Hello World')
def addNumbers(num1, num2):
	sum = num1 + num2
	return sum
    #Calling a function
    #functionName(parameters)
def helloWorld():        # Define the helloWorld function. 
    print('Hello World') 
helloWorld()            # Call to helloWorld function.
def addNumbers(num1, num2): 
	sum = num1 + num2 
	print(sum) 
	return 
addNumbers(2,3) 
addNumbers(4,5)
    #Lamba, i.e. anonymous functions, are small, restricted functions which don't need a name (lambda p1, p2: expression)
adder = lambda x, y: x + y
print (adder (1, 2))

#Section 8: Operations on Numbers and Strings
    #required import "math module" (import moduleName ex: import math)
    #To access any function of the math module we write math.functionName()
import math
math.pow(4,3)
    #math.floor() takes in a number as a parameter and returns the largest integer equal to or less than the number passed as the parameter.
import math
a = math.floor(4.3)
b = math.floor(10.9)
print (a)
print (b)
    #math.ceil() takes in a number as a parameter and returns the smallest integer equal to or greater than the number passed as the parameter.
import math 
a = math.ceil(4.3)  
b = math.ceil(10.9)  
print (a) 
print (b)
    #fabs() function takes in one parameter and returns its absolute value.
a = math.fabs(10)  
b = math.fabs(-10)  
print (a) 
print (b)
    #math.log() can take either one parameter or two.
    #When one parameter is passed it returns the natural logarithm of that number.
    #When two parameters are passed it returns the logarithm of the first number to the base of the second number.
import math 
a = math.log(10)  
b = math.log(10,2)  
print (a) 
print (b)
    #The square root of a number can be found by using math.sqrt() function.
import math 
a = math.sqrt(9)  
b = math.sqrt(16)  
print (a) 
print (b)
    #A string enclosed within triple quotes ‘’’ ‘’’ can span to multiple lines and all the whitespace will be included in the string. 
    # “”” “”” can also be used in place of ‘’’ ‘’’.
    #Capitalize() function    str.functionName()     str.count()     str.find()
str = "here I Am."
str.capitalize()
    #str.count() 
str = "here I Am."
str.count('e')
    #str.find()
    #The first character will always be at a location 0, i.e index starts from 0.
str = "here I Am." 
a = str.find("h") 
print (a) #output will be 0
    #A str.join() function returns the concatenated string of the sequence of strings passed to it.
str = " " 
iter = ("I","am","awesome.") 
a = str.join(iter) 
print(a)    #output: I am awesome.

#Section 9: Lists in Python 3
    #A variable can be used to store a list.
list1 = [2, 4, 5, 6, 7, 2]
list2 = [4, 'hi', 6, 'Me', 78]
    #The items in the list are identified using their positions. These positions are known as indexes.
list1 = [2, 4, 5, 6, 7, 2]
    #if we want to access the value 4, we must write:
list1[1] #will display "4"
    #Thus if we want to access the values 4, 5, 6 we can write:
list1 = [2, 4, 5, 6, 7, 2]
a = list1[1:4]
print(a) #will return 4, 5, 6
list1[:] #will return [2, 4, 5, 6, 7, 2]
    #Similarly, to access items beginning from index 0, we can write:
list1[:5]
    #When no index is specified before the colon, indexing starts from 0. To access the elements from index 2 till the end we can write
list2 = [4, 55, 6, 7, 8, 9, 90]
    #In order to update the value of the item at index 4 (which has value 8), we write:
list2[4] = 88
    #To add an item at the end of the list we use the append() function.
list2.append(150) #Will add 150 at the end of the list and the updated list will look like:
[4, 55, 6, 7, 88, 9, 90, 150]
    #To delete items from the list we use del statement followed by the name of the list and the index in brackets.
list1 = [4, 5, 6, 2 ,1]
del list1[3] #will return [4, 5, 6, 1]

#Section 10: Tuples in Python 3
    #A tuple is a sequence of items separated by commas.
tuple1 = (2, 4, 5, 6, 7, 2)
tuple2 = (4, 'hi', 6, 'Me', 78)
tuple1[1] #will return '4' from tuple1
tuple1 #will return (2, 4, 5, 6, 7, 2)
tuple1[:5] #will return (2, 4, 5, 6, 7, 2)
tuple1[2:] #will return (5, 6, 7, 2)
    #Unlike lists, tuples are immutable. Immutable refers to the fact that the items in a tuple cannot be updated or deleted.
del tuple1 #will delete tuple1

#Section 11: Keys and their Values
    #A dictionary is a data structure which contains data in the form of pairs of keys and values.
    #Items in a dictionary are separated by a comma. Note that the last item doesn’t have a comma following it. Keys and values are separated by a colon (:).
dict1= {'name' : 'xyz', 'age' : 25, 'hobby' : 'Dancing'}
dict1['age'] #access Key "age"
print(dict1['age']) #will print '25'
print(dict1['name']) #will print 'xyz'
print(dict1) #{'hobby': 'Dancing', 'age': 25, 'name': 'xyz'} because dictionaries are considered to be unordered data structures.
dict1['name'] = 'abc' #updates value 'name' to 'abc'
dict1['profession'] = 'pilot' #will add new key 'profession' and assign it value 'pilot'
del dict1['name'] #will delete Key and Value 'name'
del dict1 #will delete entire dictionary
dict1.clear() #will remove all items from 'dict1'


#Certificate Granted: 08/22/2023
#Document revised: 08/23/2023 by Jay M. Watson
