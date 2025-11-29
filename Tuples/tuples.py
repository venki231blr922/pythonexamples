'''
This file provides detailed guide of Python Tuples usage with examples
'''

# Tuples are used to store multiple items of various data types in a single variable
# Tuples are created with parantheses brackets
# Tuples are ORDERED, UNCHANGEABLE, DUPLICATES ALLOWED. FASTER

# Sample Tuple
fruits = ("Apple", "Banana", "Cherry", "Orange")

# Sample Tuple with various data types
a = (1, 2.0, 'string', True, [1,2], (3,4), {'name':'Jack'})

# Different methods that are available with tuples
# print(dir(fruits))
# Output of the above
# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']

# For a detailed explanation of each of the tuples method
# print(help(fruits))
# Output of the above
'''
Help on tuple object:

class tuple(object)
 |  tuple(iterable=(), /)
 |
 |  Built-in immutable sequence.
 |
 |  If no argument is given, the constructor returns an empty tuple.
 |  If iterable is specified the tuple is initialized from iterable's items.
 |
 |  If the argument is a tuple, the return value is the same object.
 |
 |  Built-in subclasses:
 |      asyncgen_hooks
 |      UnraisableHookArgs
 |
 |  Methods defined here:
 |
 |  __add__(self, value, /)
 |      Return self+value.
 |
 |  __contains__(self, key, /)
 |      Return bool(key in self).
 |
 |  __eq__(self, value, /)
 |      Return self==value.
 |
 |  __ge__(self, value, /)
 |      Return self>=value.
 |
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |
 |  __getitem__(self, key, /)
 |      Return self[key].
 |
 |  __getnewargs__(self, /)
 |
 |  __gt__(self, value, /)
 |      Return self>value.
 |
 |  __hash__(self, /)
 |      Return hash(self).
 |
 |  __iter__(self, /)
 |      Implement iter(self).
 |
 |  __le__(self, value, /)
 |      Return self<=value.
 |
 |  __len__(self, /)
 |      Return len(self).
 |
 |  __lt__(self, value, /)
 |      Return self<value.
 |
 |  __mul__(self, value, /)
 |      Return self*value.
 |
 |  __ne__(self, value, /)
 |      Return self!=value.
 |
 |  __repr__(self, /)
 |      Return repr(self).
 |
 |  __rmul__(self, value, /)
 |      Return value*self.
 |
 |  count(self, value, /)
 |      Return number of occurrences of value.
 |
 |  index(self, value, start=0, stop=9223372036854775807, /)
 |      Return first index of value.
 |
 |      Raises ValueError if the value is not present.
 |
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |
 |  __class_getitem__(object, /)
 |      See PEP 585
 |
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |
 |  __new__(*args, **kwargs)
 |      Create and return a new object.  See help(type) for accurate signature.
'''

# Accessing elements in the Tuples
# fruits = ()"Apple", "Banana", "Cherry", "Orange")
print(fruits[0]) #Apple
print(fruits[-1]) #Orange
print(fruits[:1]) # ('Apple',)
print(fruits[1:]) # ('Banana', 'Cherry', 'Orange')
print(fruits[:-1]) # ('Apple', 'Banana', 'Cherry')
print(fruits[-1:]) # ('Orange',)
print(fruits[::1]) # ('Apple', 'Banana', 'Cherry', 'Orange')
print(fruits[1::1]) # ('Banana', 'Cherry', 'Orange')
print(fruits[::2]) # ('Apple', 'Cherry')
print(fruits[::-1]) # ('Orange', 'Cherry', 'Banana', 'Apple')
print(fruits[-2::-2]) # ('Cherry', 'Apple')

num_tuple = (0,1,2,3,4,5,6,7,8,9,10)
print(f'num_tuple[:] = {num_tuple[:]}') # num_tuple[:] = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(f'num_tuple[0:5] = {num_tuple[0:5]}') # num_tuple[0:5] = (0, 1, 2, 3, 4)
print(f'num_tuple[:5] = {num_tuple[:5]}') # num_tuple[:5] = (0, 1, 2, 3, 4)
print(f'num_tuple[5:] = {num_tuple[5:]}') # num_tuple[5:] = (5, 6, 7, 8, 9,)
print(f'num_tuple[:-3] = {num_tuple[:-3]}') # num_tuple[:-3] = (0, 1, 2, 3, 4, 5, 6, 7)
print(f'num_tuple[-3:] = {num_tuple[-3:]}') # num_tuple[-3:] = (8, 9, 10)
print(f'num_tuple[::2] = {num_tuple[::2]}') # num_tuple[::2] = (0, 2, 4, 6, 8, 10)
print(f'num_tuple[1::2] = {num_tuple[1::2]}') # num_tuple[1::2] = (1, 3, 5, 7, 9)
print(f'num_tuple[2::2] = {num_tuple[2::2]}') # num_tuple[2::2] = (2, 4, 6, 8, 10)
print(f'num_tuple[::-1] = {num_tuple[::-1]}') # num_tuple[::-1] = (10, 9, 8, 7, 6, 5, 4, 3, 2, 1,)
print(f'num_tuple[5::-1] = {num_tuple[5::-1]}') # num_tuple[5::-1] = (5, 4, 3, 2, 1, 0)

# Lets try some of the tuple methods
# Length of the tuples
print(len(fruits))

# using the 'in' method, spits out True or False, Depends of whether the string case-sensitive
print("Apple" in fruits) # woruld return True
print("apple" in fruits) # woruld return False




# Index the tuples using 'index' method. Index method gives us the index of the value in the tuples
print(fruits.index("Cherry"))
# 3 Thats the index of the value 'cherry' in the tuples

# Count the values using 'count' method. Count method gives us the count of the values in the tuples
print(fruits.count("Pineapple"))
# 2 Thats the count of the value 'Pineapple' in the tuples

# Operators in tuples
tuple1 = (1,2,3)
tuple2 = (4,5,6)
tuple3 = (1,2,3)
print(f'tuple1 + tuple2 = {tuple1 + tuple2}') # tuple1 + tuple2 = (1, 2, 3, 4, 5, 6)
print(f'tuple1 * 3 = {tuple1 * 3}') # tuple1 * 3 = (1, 2, 3, 1, 2, 3, 1, 2, 3)
print(f'tuple1 == tuple3 -> {tuple1 == tuple3}') # tuple1 == tuple3 -> True
print(f'tuple1 != tuple2 -> {tuple1 != tuple2}') # tuple1 != tuple2 -> True
print(f'tuple1 < tuple3 -> {tuple1 < tuple3}') # tuple1 < tuple3 -> False
print(f'tuple1 <= tuple3 -> {tuple1 <= tuple3}') # tuple1 <= tuple3 -> True
print(f'tuple1 > tuple3 -> {tuple1 > tuple3}') # tuple1 > tuple3 -> False
print(f'tuple1 >= tuple3 -> {tuple1 >= tuple3}') # tuple1 >= tuple3 -> True
print(f'1 in tuple1 -> {1 in tuple1}') # 1 in tuple1 -> True
print(f'8 not in tuple3 -> {8 not in tuple3}') # 8 not in tuple3 -> True

# shallow copy
ref_tuple1 = (1,2,3,[4,5])
ref_tuple2 = ref_tuple1
print(id(ref_tuple1)) # memory address 1805897022448
print(id(ref_tuple2)) # memory address 1805897022448, both refer to the same memory address

shal_tuple1 = (1,2,3,[4,5])
shal_tuple2 = shal_tuple1[:]
print(id(shal_tuple1)) # memory address 1805897022288
print(id(shal_tuple2)) # same memory address 1805897022288 but have identical values in the tuple

shal_tuple2[3][0] = 'A'
shal_tuple2[3][1] = 'B'

print(shal_tuple1) # (1, 2, 3, ['A', 'B']) we replaced the values in shal_tuple2, but since we had sha1_tuple2 = shal_tuple1[:], results in shal_tuple1 will get affected

# Tuple loops
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

# apple
# banana
# cherry

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

# apple
# banana
# cherry