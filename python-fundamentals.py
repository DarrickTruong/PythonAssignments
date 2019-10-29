
# print
name = "Zen"
print("My name is", name)

# concatenation
name = "Zen"
print("My name is " + name)


# F-Strings (Literal String Interpolation) -- print string with integer in string
first_name = "Zen"
last_name = "Coder"
age = 27
print(f"My name is {first_name} {last_name} and I am {age} years old.")


first_name = "Zen"
last_name = "Coder"
age = 27
print("My name is {} {} and I am {} years old.".format(first_name, last_name, age))
# output: My name is Zen Coder and I am 27 years old.
print("My name is {} {} and I am {} years old.".format(age, first_name, last_name))
# output: My name is 27 Zen and I am Coder years old.


# % formatting
# Here is an even older method of string interpolation that you may come across when troubleshooting or researching, 
# so you should know about it. Rather than curly braces, the % symbol is used to indicate a placeholder, a %s for a string and %d for a number.
# After the string, a single % separates the string to be interpolated from the values to be inserted into the string, like so:
hw = "Hello %s" % "world" 	# with literal values
py = "I love Python %d" % 3 
print(hw, py)
# output: Hello world I love Python 3
name = "Zen"
age = 27
print("My name is %s and I'm %d" % (name, age))		# or with variables
# output: My name is Zen and I'm 27


# string.upper()
cheese = "i like cheese".upper()
print(cheese)















#Primitive Data Types

# Boolean Values - Assesses the truth value of something. It has only two values: True and False (note the uppercase T and F)
is_hungry = True
has_freckles = False

# Numbers - Integers (whole numbers), floating point numbers (commonly known as decimal numbers), and complex numbers
age = 35 # storing an int
weight = 160.57 # storing a float

# Strings - literal text
name = "Joe Blue"



#Composite Types

# Tuples - A type of data that is immutable (can't be modified after its creation) and can hold a group of values. Tuples can contain mixed data types.
dog = ('Bruce', 'cocker spaniel', 19, False)
print(dog[0])		# output: Bruce
dog[1] = 'dachshund'	# ERROR: cannot be modified ('tuple' object does not support item assignment)

# Lists - A type of data that is mutable and can hold a group of values. Usually meant to store a collection of related data.
empty_list = []
ninjas = ['Rozen', 'KB', 'Oliver']
print(ninjas[2]) 	# output: Oliver
ninjas[0] = 'Francis'
ninjas.append('Michael')
print(ninjas)	# output: ['Francis', 'KB', 'Oliver', 'Michael']
ninjas.pop()
print(ninjas)	# output: ['Francis', 'KB', 'Oliver']
ninjas.pop(1)
print(ninjas)	# output: ['Francis', 'Oliver']

# Dictionaries - A group of key-value pairs. Dictionary elements are indexed by unique keys which are used to access values. 
# When you're ready, you can find more built-in dictionary methods here -- https://www.w3schools.com/python/python_ref_dictionary.asp
empty_dict = {}
new_person = {'name': 'John', 'age': 38, 'weight': 160.2, 'has_glasses': False}
new_person['name'] = 'Jack'	# updates if the key exists
new_person['hobbies'] = ['climbing', 'coding']	# adds a key-value pair if the key doesn't exist
print(new_person)	
# output: {'name': 'Jack', 'age': 38, 'weight': 160.2, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}
w = new_person.pop('weight')	# removes the specified key and returns the value
print(w)		# output: 160.2
print(new_person)	
# output: {'name': 'Jack', 'age': 38, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}        

# Type Casting or Explicit Type Conversion
print("Hello" + 42)			# output: TypeError
print("Hello" + str(42))		# output: Hello 42

total = 35
user_val = "26"
total = total + user_val		# output: TypeError
total = total + int(user_val)		# total will be 61

# type function
print(type(2.63))		# output: <class 'float'>
print(type(new_person))		# output: <class 'dict'>



# Interate Dictionaries
my_dict = { "name": "Noelle", "language": "Python" }
for k in my_dict:
    print(k)
# output: name, language

my_dict = { "name": "Noelle", "language": "Python" }
for k in my_dict:
    print(my_dict[k])
# output: Noelle, Python

# another way to iterate through the keys
for key in capitals.keys():
     print(key)
#to iterate through the values
for val in capitals.values():
     print(val)
#to iterate through both keys and values
for key, val in capitals.items():
     print(key, " = ", val)
















#Loops

# For Loops with Range
for x in range(0, 10, 2):
    print(x)
# output: 0, 2, 4, 6, 8
for x in range(5, 1, -3):
    print(x)
# output: 5, 2


# For Loops through Lists
my_list = ["abc", 123, "xyz"]
for i in range(0, len(my_list)):
    print(i, my_list[i])
# output: 0 abc, 1 123, 2 xyz
    
# OR 
    
for v in my_list:
    print(v)
# output: abc, 123, xyz


# For Loops through Dictionaries
my_dict = { "name": "Noelle", "language": "Python" }
for k in my_dict:
    print(k)
# output: name, language


my_dict = { "name": "Noelle", "language": "Python" }
for k in my_dict:
    print(my_dict[k])
# output: Noelle, Python


# another way to iterate through the keys
for key in capitals.keys():
     print(key)
#to iterate through the values
for val in capitals.values():
     print(val)
#to iterate through both keys and values
for key, val in capitals.items():
     print(key, " = ", val)



# While Loops -- While loops are another way of looping while a certain condition is true.
# while <expression>:
    # do something, including progress towards making the expression False. Otherwise we'll never get out of here!

count = 0
while count < 5:
    print("looping - ", count)
    count += 1


#Else
# There are certain conditions that we give for every loop that we have, but what if the condition was not met and we still would like to do something if that happens? 
# We can then use an else statement with our while loop. Yes, that is right, else in a loop.
y = 3
while y > 0:
    print(y)
    y = y - 1
else:
    print("Final else statement")


# Loop Control

# Break
for val in "string":
    if val == "i":
        break
    print(val)
# output: s, t, r


# Continue
# The continue statement immediately returns control to the beginning of the loop. In other words, the continue statement rejects, 
# or skips, all the remaining statements in the current iteration of the loop, and continues normal execution at the top of the loop.
# The continue statement is very useful when you want to skip specific iteration(s), but still keep looping to the end.
for val in "string":
    if val == "i":
        continue
    print(val)
# output: s, t, r, n, g
# notice, no i in the output, but the loop continued after the i

y = 3
while y > 0:
    print(y)
    y = y - 1
    if y == 0:
        break
else:		# only executes on a clean exit from the while loop (i.e. not a break)
   print("Final else statement")
# output: 3, 2, 1













#Functions
# Wait, but what's the difference between a parameter and an argument? These two words get mixed up a lot in programming. 
# In this example 'name' is a parameter while "Michael", "Anna", and "Eli", are arguments. We define parameters. We pass in arguments into functions.
def say_hi(name):
    print("Hi, " + name)
# invoking the function 3 times, passing in one argument each time
say_hi('Michael')
say_hi('Anna')
say_hi('Eli')


# Default Parameters
def beCheerful(name='', repeat=2):		# set defaults when declaring the parameters
	print(f"good morning {name}\n" * repeat)
beCheerful()				# output: good morning (repeated on 2 lines)
beCheerful("tim")		        # output: good morning tim (repeated on 2 lines)
beCheerful(name="john")			# output: good morning john (repeated on 2 lines)
beCheerful(repeat=6)			# output: good morning (repeated on 6 lines)
beCheerful(name="michael", repeat=5)	# output: good morning michael (repeated on 5 lines)
# NOTE: argument order doesn't matter if we are explicit when sending in our arguments!
beCheerful(repeat=3, name="kb")		# output: good morning kb (repeated on 3 lines)











# Python Swap
# python code below!
arr = [1,3,5,7]
arr[0], arr[1] = arr[1], arr[0]
