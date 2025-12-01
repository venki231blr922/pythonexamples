'''
 This file provides detailed guide of python functions with examples
'''

# A function is a block of code which only runs when called
# A function can return data as result
# A function hels avoiding code repition

# Creating a function
# In python, a function is defined using the def keyword, followed by a function name and parentheses
# The code inside the function must be indented. Python uses indentation to define code blocks.

def my_function():
  print("Hello from a function")

# Calling the above function spits out the "Hello from a function", you call the same function multiple times if you like
my_function()
my_function()
my_function()

# Function Arguments
'''
Information can be passed into functions as an argument.
Arguments are specified after the function name, inside the parenthese. You can add as many arguments as you want, seperated by comma. 
'''
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

# Emil Refsnes
# Tobias Refsnes
# Linus Refsnes

# Parameter vs Arguments
# The terms parameter and arguments can be used for the same thing: information that are passed into function.
# From a functions perspective: a parameter is the variable inside the parenthese in the function definition
# An argument is the actual value that is sent to the function when it is called

def my_function(name): # name is a parameter
  print("Hello", name)

my_function("Emil") # "Emil" is an argument

# Number of arguments
# by default, a function must be called with the correct number of arguments
# if your function expects 2 arguments, you must call it with 2 arguments
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

# wrong arguments passed, expects 2 arguments and ends up throwing an error
'''
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil")
'''

# #     my_function("Emil")
#     ~~~~~~~~~~~^^^^^^^^
# TypeError: my_function() missing 1 required positional argument: 'lname'

# Default parameter values
# you can assign default values to parameters, when functions is called without argument, uses the default value

def my_function(name = "Friend"):
  print("Hello", name)

my_function("Emil")
my_function()

# Hello Emil
# Hello Friend

# Keyword arguments
# you can send arguments with the key = value syntax
# with keyword arguments, the order of the arguments does not matter.
# The phrase Keyword Arguments is often shortened to kwargs

def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(name = "Buddy", animal = "dog")

# I have a dog
# My dog's name is Buddy

# Positional arguments
# When you call function without keyword arguments, they are called positional arguments
# Positional arguments must be in correct order.

def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("dog", "Buddy")
# I have a dog
# My dog's name is Buddy

# Switching the order, changes the result
my_function("Buddy", "dog")
# I have a Buddy
# My Buddy's name is dog

# Mixing positional and keyword arguments
# you can mix positional and keyword arguments in a function call
# However, positional arguments must come before keyword arguments.

def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "Buddy", age = 5)
# I have a 5 year old dog named Buddy

# Passing different data types
# You can send any data type as an argument to a function ( string, number, list, dict, etc...)
# The data type will be preserved inside the function

def my_function(fruits):
    for fruit in fruits:
        print(fruit)

my_fruits = ["apple", "banana", "orange"] # passing a list as an argument
my_function(my_fruits)
# apple
# banana
# orange

def my_function(person):
    print("Name:", person["name"])
    print("Age:", person["age"])
    
my_person = {"name": "Email", "age": 25}
my_function(my_person)

# Name: Email
# Age: 25

# Return values
# functions can return values using the return statement

def my_function(x, y):
  return x + y

result = my_function(5, 3)
print(result) # 8

# Returning different data types 
# functions can return any data types, including lists, tuples, dicts and more

# function that returns a lists
def my_function():
  return ["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])

# apple
# banana
# cherry

# function that returns a tuples
def my_function():
  return (10, 20)

x, y = my_function()
print("x:", x)
print("y:", y)
# x: 10
# y: 20

# Positoonal only arguments
# you can specify that a function can ONLY have positional arguments, add , / after the arguments

def my_function(name, /):
  print("Hello", name)

my_function("Emil") # Hello Emil
# my_function(name = "John") # will error out

#     ~~~~~~~~~~~^^^^^^^^^^^^^^^
# TypeError: my_function() got some positional-only arguments passed as keyword arguments: 'name'

# Keyword only arguments
# To specify a function to have ONLY keyword as arguments, add *, before the arguments

def my_function(*, name):
  print("Hello", name)

my_function(name = "Emil") # Hello Emil
# my_function("Emil") # TypeError: my_function() takes 0 positional arguments but 1 was given

# Combining positional-only and keyword-only 
# you can combine both argument types in same function
# Arguments before / are positional-only and arguments after * are keyword only
def my_function(a, b, /, *, c, d):
  return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
print(result)


# *args  and *kwargs

# by default, a function must be called with the correct number of arguments
# however, sometimes you may not know how many arguments that will be passed into your function
# *args and *kwargs allow functions to accept a unknown number of arguments

# the below function will receieve a tuple of arguments and can access the items accordingly.
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

# using *args with regular functions
def my_function(greeting, *names):
  for name in names:
    print(greeting, name)

my_function("Hello", "Emil", "Tobias", "Linus")

# practical example with *args
def my_function(*numbers):
  if len(numbers) == 0:
    return None
  max_num = numbers[0]
  for num in numbers:
    if num > max_num:
      max_num = num
  return max_num

print(my_function(3, 7, 2, 9, 1))

# Arbitary keyword arguments **kwargs
# similar to *args this one is for keyword arguments, if you are unsure of how many keyword arguments in function
# below sample function can accept any number of keyword arguments
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

# accessing values with **kwargs
def my_function(**myvar):
  print("Type:", type(myvar))
  print("Name:", myvar["name"])
  print("Age:", myvar["age"])
  print("All data:", myvar)

my_function(name = "Tobias", age = 30, city = "Bergen")

# Type: <class 'dict'>
# Name: Tobias
# Age: 30
# All data: {'name': 'Tobias', 'age': 30, 'city': 'Bergen'}

# Using **kwargs with regualr arguments
def my_function(username, **details):
  print("Username:", username)
  print("Additional details:")
  for key, value in details.items():
    print(" ", key + ":", value)

my_function("emil123", age = 25, city = "Oslo", hobby = "coding")

# Username: emil123
# Additional details:
#   age: 25
#   city: Oslo
#   hobby: coding

# Combining *args and **kwargs 
# you can use both *args and **kwargs in the same function
# order must be
# 1. regular arguments
# 2. *args
# 3. **kwargs

def my_function(title, *args, **kwargs):
  print("Title:", title)
  print("Positional arguments:", args)
  print("Keyword arguments:", kwargs)

my_function("User Info", "Emil", "Tobias", age = 25, city = "Oslo")

# unpacking arguments
# * and ** operators can also be used when calling functions to unpack a list or dict into seperate arguments

# unpacking lists with *
# if you have values stored in lists, you can use * to unpack them into individual arguments
def my_function(a, b, c):
  return a + b + c

numbers = [1, 2, 3]
result = my_function(*numbers) # Same as: my_function(1, 2, 3)
print(result) # 6

# unpacking dicts
# use ** to unpack keyword arguments
def my_function(fname, lname):
  print("Hello", fname, lname)

person = {"fname": "Emil", "lname": "Refsnes"}
my_function(**person) # Same as: my_function(fname="Emil", lname="Refsnes")
# Hello Emil Refsnes



# Scope
# Local scope
# A variable created inside a function belongs to the local scope of that fucntion and can only be used inside that function

def myFunc():
    x = 300
    print(x)

myFunc()

# function inside a function
# the above example variable x is not available outside function, but is available inside the any function inside fucntion

def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()


# Global scope
# A vairable created in the main body of the python code and belongs to global scope
# they are avilable from within any scope, global and local

x = 300

def myfunc():
  print(x)

myfunc()

print(x)

# Naming variables
# if you operate the same variable name inside and outside a function, python will treat them as two diff variables, one available in global scope and one available in local scope ( inside function )
x = 300 # global

def myfunc():
  x = 200 # local
  print(x)

myfunc() # local scope

print(x) # global scope

# 200
# 300

# Global keyword
# if you need to create a global variable but are stuck in the local scope, use global keyword

def myfunc():
  global x
  x = 300

myfunc()

print(x)

# you can also change the value of global variable inside the function
x = 300

def myfunc():
  global x
  x = 200

myfunc()

print(x)


# nonlocal keyword
# if you use nonlocal keyword, the variable will belong to the outer function

def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1()) # hello

# LEGB rule, python follows this rule when looking up variables names and searches for then in order.
# 1. Local - inside function
# 2. Enclosing - inside enclosing functions ( from inner to outer)
# 3. Global - at the top level of the module
# 4. Built-in -  in python's built in namespace

x = "global"

def outer():
  x = "enclosing"
  def inner():
    x = "local"
    print("Inner:", x)
  inner()
  print("Outer:", x)

outer()
print("Global:", x)

# Inner: local
# Outer: enclosing
# Global: global

