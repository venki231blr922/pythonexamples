'''
    This file guides you on the Python decorators with usage examples
'''

# Decorators lets you add extra behaviour to a function, without changing the functions code.
# a decorator is a function that takes another function as input and returns a new function

# Basic Decorator
# define the decorator first , then apply with @decorator_name above the function

def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

print(myfunction()) # HELLO SALLY

# The function changecase is the decorator.
# The function myfunction is the function that gets decorated.

# Multiple decorator calls
# they can be called multiple times

def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

@changecase
def otherfunction():
  return "I am speed!"

print(myfunction())
print(otherfunction())
# HELLO SALLY
# I AM SPEED!

# functions with arguments can be decorated

def changecase(func):
  def myinner(x):
    return func(x).upper()
  return myinner

@changecase
def myfunction(nam):
  return "Hello " + nam

print(myfunction("John")) # HELLO JOHN

# Secure the function with *args and **kwargs arguments:

def changecase(func):
  def myinner(*args, **kwargs):
    return func(*args, **kwargs).upper()
  return myinner

@changecase
def myfunction(nam):
  return "Hello " + nam

print(myfunction("John"))

# Decorator with arguments
# A decorator factory that takes an argument and transforms the casing based on the argument value.

def changecase(n):
  def changecase(func):
    def myinner():
      if n == 1:
        a = func().lower()
      else:
        a = func().upper()
      return a
    return myinner
  return changecase

@changecase(1)
def myfunction():
  return "Hello Linus"

print(myfunction()) # hello linus

# Mutliple decorators
# you can use multiple decorators on one function
# This is done by placing the decorator calls on top of each other.
# Decorators are called in the reverse order, starting with the one closest to the function.

def changecase(func):
    def myinner():
        return func().upper()
    return myinner

def addgreeting(func):
    def myinner():
        return "Hello " + func() + " Have a good day!"
    return myinner

@changecase
@addgreeting
def myFunction():
    return "Tobias"

print(myFunction()) # HELLO TOBIAS HAVE A GOOD DAY!

