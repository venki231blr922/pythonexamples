'''
This file provides detailed guide of Python Lists usage with examples
'''

# Lists are used to store multiple items of various data types in a single variable
# Lists are created with square brackets
# Lists are ORDERED, CHANGEABLE, DUPLICATES ALLOWED

# Sample Lists
fruits = ["Apple", "Banana", "Cherry", "Orange"]

# Sample Lists with various data types
a = [1, 2.0, 'string', True, [1,2], (3,4), {'name':'Jack'}]

# Different methods that are available with Lists
# print(dir(fruits))
# Output of the above
# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

# For a detailed explanation of each of the Lists method
# print(help(fruits))
# Output of the above
'''
Help on list object:

class list(object)
 |  list(iterable=(), /)
 |
 |  Built-in mutable sequence.
 |
 |  If no argument is given, the constructor creates a new empty list.
 |  The argument must be an iterable if specified.
 |
 |  Methods defined here:
 |
 |  __add__(self, value, /)
 |      Return self+value.
 |
 |  __contains__(self, key, /)
 |      Return bool(key in self).
 |
 |  __delitem__(self, key, /)
 |      Delete self[key].
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
 |  __getitem__(self, index, /)
 |      Return self[index].
 |
 |  __gt__(self, value, /)
 |      Return self>value.
 |
 |  __iadd__(self, value, /)
 |      Implement self+=value.
 |
 |  __imul__(self, value, /)
 |      Implement self*=value.
 |
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
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
 |  __reversed__(self, /)
 |      Return a reverse iterator over the list.
 |
 |  __rmul__(self, value, /)
 |      Return value*self.
 |
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |
 |  __sizeof__(self, /)
 |      Return the size of the list in memory, in bytes.
 |
 |  append(self, object, /)
 |      Append object to the end of the list.
 |
 |  clear(self, /)
 |      Remove all items from list.
 |
 |  copy(self, /)
 |      Return a shallow copy of the list.
 |
 |  count(self, value, /)
 |      Return number of occurrences of value.
 |
 |  extend(self, iterable, /)
 |      Extend list by appending elements from the iterable.
 |
 |  index(self, value, start=0, stop=9223372036854775807, /)
 |      Return first index of value.
 |
 |      Raises ValueError if the value is not present.
 |
 |  insert(self, index, object, /)
 |      Insert object before index.
 |
 |  pop(self, index=-1, /)
 |      Remove and return item at index (default last).
 |
 |      Raises IndexError if list is empty or index is out of range.
 |
 |  remove(self, value, /)
 |      Remove first occurrence of value.
 |
 |      Raises ValueError if the value is not present.
 |
 |  reverse(self, /)
 |      Reverse *IN PLACE*.
 |
 |  sort(self, /, *, key=None, reverse=False)
 |      Sort the list in ascending order and return None.
 |
 |      The sort is in-place (i.e. the list itself is modified) and stable (i.e. the
 |      order of two equal elements is maintained).
 |
 |      If a key function is given, apply it once to each list item and sort them,
 |      ascending or descending, according to their function values.
 |
 |      The reverse flag can be set to sort in descending order.
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

# Accessing elements in the lists
# fruits = ["Apple", "Banana", "Cherry", "Orange"]
print(fruits[0]) #Apple
print(fruits[-1]) #Orange
print(fruits[:1]) #Apple
print(fruits[1:]) #['Banana', 'Cherry', 'Orange']
print(fruits[:-1]) # ['Apple', 'Banana', 'Cherry']
print(fruits[-1:]) # ['Orange']
print(fruits[::1]) # ['Apple', 'Banana', 'Cherry', 'Orange']
print(fruits[1::1]) # ['Banana', 'Cherry', 'Orange']
print(fruits[::2]) # ['Apple', 'Cherry']
print(fruits[::-1]) # ['Orange', 'Cherry', 'Banana', 'Apple']
print(fruits[-2::-2]) # ['Cherry', 'Apple']

num_list = [0,1,2,3,4,5,6,7,8,9,10]
print(f'num_list[:] = {num_list[:]}') # num_list[:] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f'num_list[0:5] = {num_list[0:5]}') # num_list[0:5] = [0, 1, 2, 3, 4]
print(f'num_list[:5] = {num_list[:5]}') # num_list[:5] = [0, 1, 2, 3, 4]
print(f'num_list[5:] = {num_list[5:]}') # num_list[5:] = [5, 6, 7, 8, 9, 10]
print(f'num_list[:-3] = {num_list[:-3]}') # num_list[:-3] = [0, 1, 2, 3, 4, 5, 6, 7]
print(f'num_list[-3:] = {num_list[-3:]}') # num_list[-3:] = [8, 9, 10]
print(f'num_list[::2] = {num_list[::2]}') # num_list[::2] = [0, 2, 4, 6, 8, 10]
print(f'num_list[1::2] = {num_list[1::2]}') # num_list[1::2] = [1, 3, 5, 7, 9]
print(f'num_list[2::2] = {num_list[2::2]}') # num_list[2::2] = [2, 4, 6, 8, 10]
print(f'num_list[::-1] = {num_list[::-1]}') # num_list[::-1] = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(f'num_list[5::-1] = {num_list[5::-1]}') # num_list[5::-1] = [5, 4, 3, 2, 1, 0]

# Lets try some of the List methods
# Length of the Lists
print(len(fruits))

# using the 'in' method, spits out True or False, Depends of whether the string case-sensitive
print("Apple" in fruits) # woruld return True
print("apple" in fruits) # woruld return False

# Update the value in Lists
fruits[0] = "Pineapple"
print(fruits)

# Append new value in Lists using 'append' method. Always appends to the end of the list
fruits.append("Pineapple")
print(fruits)
# ['Pineapple', 'Banana', 'Cherry', 'Orange', 'Pineapple'] notice the duplicate value in the Lists, it's allowed to have duplicates

# Remove value in Lists using 'remove' method. Always removes the value from the left or starting from index o if duplicates are present
fruits.remove("Pineapple") # You could also use the 'Del" method like "del fruits[0]"
print(fruits)
# ['Banana', 'Cherry', 'Orange', 'Pineapple']

# Insert value in Lists using 'insert' method. Insert method allows to specify the index and the value to be inserted in Lists
fruits.insert(1, "Pineapple")
print(fruits)
# ['Banana', 'Pineapple', 'Cherry', 'Orange', 'Pineapple'] Notice the 'Pineapple' being inserted at index[1]

# Sort Lists using 'sort' method. Sort method sorts the values alphabetically or numerically
fruits.sort()
print(fruits)
# ['Banana', 'Cherry', 'Orange', 'Pineapple', 'Pineapple'] Alphabetically sorted

# Reverse the Lists using 'reverse' method. Reverse method gives us the reverse order of the Lists, it doesn't sort
fruits.reverse()
print(fruits)
# ['Pineapple', 'Pineapple', 'Orange', 'Cherry', 'Banana'] Reversed the Lists

# Index the Lists using 'index' method. Index method gives us the index of the value in the Lists
print(fruits.index("Cherry"))
# 3 Thats the index of the value 'cherry' in the Lists

# Count the values using 'count' method. Count method gives us the count of the values in the Lists
print(fruits.count("Pineapple"))
# 2 Thats the count of the value 'Pineapple' in the Lists

# Pop the values using 'pop' method. pop method removes the last element/value in the Lists
print(fruits.pop())
# Banana will be popped from the list ['Pineapple', 'Pineapple', 'Orange', 'Cherry', 'Banana']

# Clear the Lists using 'clear' method. Clear method clears all the values in Lists.
fruits.clear()
print(fruits)
# [] Cleared the values in the Lists


# Operators in Lists
list1 = [1,2,3]
list2 = [4,5,6]
list3 = [1,2,3]
print(f'list1 + list2 = {list1 + list2}') # list1 + list2 = [1, 2, 3, 4, 5, 6]
print(f'list1 * 3 = {list1 * 3}') # list1 * 3 = [1, 2, 3, 1, 2, 3, 1, 2, 3]
print(f'lists1 == list3 -> {list1 == list3}') # lists1 == list3 -> True
print(f'lists1 != list2 -> {list1 != list2}') # lists1 != list2 -> True
print(f'lists1 < list3 -> {list1 < list3}') # lists1 < list3 -> False
print(f'lists1 <= list3 -> {list1 <= list3}') # lists1 <= list3 -> True
print(f'lists1 > list3 -> {list1 > list3}') # lists1 > list3 -> False
print(f'lists1 >= list3 -> {list1 >= list3}') # lists1 >= list3 -> True
print(f'1 in list1 -> {1 in list1}') # 1 in list1 -> True
print(f'8 not in list3 -> {8 not in list3}') # 8 not in list3 -> True


# shallow copy
ref_list1 = [1,2,3,[4,5]]
ref_list2 = ref_list1
print(id(ref_list1)) # memory address 1973392882304
print(id(ref_list2)) # memory address 1973392882304, both refer to the same memory address

shal_list1 = [1,2,3,[4,5]]
shal_list2 = shal_list1[:]
print(id(shal_list1)) # memory address 2025502915264
print(id(shal_list2)) # different memory address 2025502915072 but have identical values in the list

shal_list2[3][0] = 'A'
shal_list2[3][1] = 'B'

print(shal_list1) # [1, 2, 3, ['A', 'B']] we replaced the values in shal_list2, but since we had sha1_list2 = shal_lis1[:], results in shal_list1 will get affected

# List comprehension
list1 = [0,1,2,3,4,5,6,7,8,9,10]
list2 = list1[:]
print(list2) # result will be [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# regular for loop with lists
list3 = []
for i in list2:
    list3.append(i)
print(list3) # result will be [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Lists comprehension being used below
list4 = [i for i in list3]
print(list4) # result will be [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list5 = [i for i in list4 if i%2 == 0]
print(list5) # result will be [0, 2, 4, 6, 8, 10]

list6 = [i*2 for i in list5 ]
print(list6)# result will be [0, 4, 8, 12, 16, 20]

# Multidimensional Lists
mlist = [[1,2,3], [4,5,6], [7,8,9]]
for r in mlist:
    print(r)
# result for above will be 
# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]
print(mlist[0][1]) # 2
print(mlist[1][0]) # 4