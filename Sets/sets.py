'''
This file provides detailed guide of Python Sets usage with examples
'''

# Sets are used to store multiple items of various data types in a single variable
# Sets are created with curly brackets
# Sets are UNORDERED, IMMUTABLE ( Meaning we can't alter values), ADD/REMOVE Elements are Allowed, DUPLICATES NOT ALLOWED

# Sample Sets
fruits = {"Apple", "Banana", "Cherry", "Orange"}

# Sample Sets with various data types
a = {1, 2.0, 'string', True, (3,4)} # we can't use Lists or Dictonaries

# Different methods that are available with Sets
# print(dir(fruits))
# Output of the above
# ['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']

# For a detailed explanation of each of the Sets method
# print(help(fruits))
# Output of the above
'''
Help on set object:

class set(object)
 |  set(iterable=(), /)
 |
 |  Build an unordered collection of unique elements.
 |
 |  Methods defined here:
 |
 |  __and__(self, value, /)
 |      Return self&value.
 |
 |  __contains__(self, object, /)
 |      x.__contains__(y) <==> y in x.
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
 |  __gt__(self, value, /)
 |      Return self>value.
 |
 |  __iand__(self, value, /)
 |      Return self&=value.
 |
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  __ior__(self, value, /)
 |      Return self|=value.
 |
 |  __isub__(self, value, /)
 |      Return self-=value.
 |
 |  __iter__(self, /)
 |      Implement iter(self).
 |
 |  __ixor__(self, value, /)
 |      Return self^=value.
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
 |  __ne__(self, value, /)
 |      Return self!=value.
 |
 |  __or__(self, value, /)
 |      Return self|value.
 |
 |  __rand__(self, value, /)
 |      Return value&self.
 |
 |  __reduce__(self, /)
 |      Return state information for pickling.
 |
 |  __repr__(self, /)
 |      Return repr(self).
 |
 |  __ror__(self, value, /)
 |      Return value|self.
 |
 |  __rsub__(self, value, /)
 |      Return value-self.
 |
 |  __rxor__(self, value, /)
 |      Return value^self.
 |
 |  __sizeof__(self, /)
 |      S.__sizeof__() -> size of S in memory, in bytes.
 |
 |  __sub__(self, value, /)
 |      Return self-value.
 |
 |  __xor__(self, value, /)
 |      Return self^value.
 |
 |  add(self, object, /)
 |      Add an element to a set.
 |
 |      This has no effect if the element is already present.
 |
 |  clear(self, /)
 |      Remove all elements from this set.
 |
 |  copy(self, /)
 |      Return a shallow copy of a set.
 |
 |  difference(self, /, *others)
 |      Return a new set with elements in the set that are not in the others.
 |
 |  difference_update(self, /, *others)
 |      Update the set, removing elements found in others.
 |
 |  discard(self, object, /)
 |      Remove an element from a set if it is a member.
 |
 |      Unlike set.remove(), the discard() method does not raise
 |      an exception when an element is missing from the set.
 |
 |  intersection(self, /, *others)
 |      Return a new set with elements common to the set and all others.
 |
 |  intersection_update(self, /, *others)
 |      Update the set, keeping only elements found in it and all others.
 |
 |  isdisjoint(self, other, /)
 |      Return True if two sets have a null intersection.
 |
 |  issubset(self, other, /)
 |      Report whether another set contains this set.
 |
 |  issuperset(self, other, /)
 |      Report whether this set contains another set.
 |
 |  pop(self, /)
 |      Remove and return an arbitrary set element.
 |
 |      Raises KeyError if the set is empty.
 |
 |  remove(self, object, /)
 |      Remove an element from a set; it must be a member.
 |
 |      If the element is not a member, raise a KeyError.
 |
 |  symmetric_difference(self, other, /)
 |      Return a new set with elements in either the set or other but not both.
 |
 |  symmetric_difference_update(self, other, /)
 |      Update the set, keeping only elements found in either set, but not in both.
 |
 |  union(self, /, *others)
 |      Return a new set with elements from the set and all others.
 |
 |  update(self, /, *others)
 |      Update the set, adding elements from all others.
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
 |
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |
 |  __hash__ = None
'''

# Accessing elements in the SETS
# fruits = {"Apple", "Banana", "Cherry", "Orange"}
# print(fruits[0]) # You would get a type error because sets are UNORDERED, so no accessing element via Index -  TypeError: 'set' object is not subscriptable

# Lets try some of the SETS methods
# Length of the Sets
print(len(fruits))

# using the 'in' method, spits out True or False, Depends of whether the string case-sensitive
print("Apple" in fruits) # woruld return True
print("apple" in fruits) # woruld return False


# Remove value in Sets using 'remove' method. Always removes the value from the left or starting from index o if duplicates are present
fruits.remove("Orange") # You could also use the 'Del" method like "del fruits[0]"
print(fruits)
# {'Apple', 'Cherry', 'Banana'}

# Insert value in Sets using 'insert' method. Insert method allows the value to be inserted at the end in Sets, 
fruits.add("Orange")
print(fruits)
# {'Apple', 'Cherry', 'Banana', 'Orange'}  Notice the 'Orabge' being inserted at last

# check the class type
print(type(fruits))
# <class 'set'>

# Pop the values using 'pop' method. pop method removes the random element/value in the Sets
print(fruits.pop())
# Apple will be popped from the list {'Apple', 'Cherry', 'Banana', 'Orange'} , first element is popped

# Clear the Sets using 'clear' method. Clear method clears all the values in Sets.
fruits.clear()
print(fruits)
# set() Cleared the values in the Lists

# Operators in Sets
set1 = {1,2,3}
set2 = {4,5,6}
set3 = {1,2,3}
print(f'set1 union set2 = {set1.union(set2)}') # set1 union set2 = {1, 2, 3, 4, 5, 6}
print(f'set1 | set2 = {set1 | set2 }') # set1 | set2 = {1, 2, 3, 4, 5, 6}
print(f'set1 == set3 -> {set1 == set3}') # set1 == set3 -> True
print(f'set1 != set2 -> {set1 != set2}') # set1 != set2 -> True
print(f'set1 < set3 -> {set1 < set3}') # set1 < set3 -> False
print(f'set1 <= set3 -> {set1 <= set3}') # set1 <= set3 -> True
print(f'set1 > set3 -> {set1 > set3}') # set1 > set3 -> False
print(f'set1 >= set3 -> {set1 >= set3}') # set1 >= set3 -> True
print(f'1 in set1 -> {1 in set1}') # 1 in set1 -> True
print(f'8 not in set3 -> {8 not in set3}') # 8 not in set3 -> True
set1.update(set2) 
print(f'set1 = {set1}') # set1 = {1, 2, 3, 4, 5, 6}

# shallow copy
ref_set1 = {1,2,3,4,5}
ref_set2 = ref_set1
print(id(ref_set1)) # memory address 1216090498080
print(id(ref_set2)) # memory address 1216090498080, both refer to the same memory address

# Sets comprehension
set1 = {0,1,2,3,4,5,6,7,8,9,10}
set2 = set1
print(set2) # result will be {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# Sets comprehension being used below
set3 = {i for i in set2}
print(set3) # result will be {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

set4 = {i for i in set3 if i%2 == 0}
print(set4) # result will be {0, 2, 4, 6, 8, 10}

set5 = {i*2 for i in set4 }
print(set5)# result will be {0, 4, 8, 12, 16, 20}

# Multidimensional Sets , Allows only tuples to be used ( Not Allowed in sets: Lists,Sets,Dicts)
mlist = {(1,2),(3,4),(5,6)}
for r in mlist:
    print(r)
# (1, 2)
# (3, 4)
# (5, 6)