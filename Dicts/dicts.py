'''
This file provides detailed guide of Python Dictionaries usage with examples
'''

# Dicts are used to store data values in key:value pairs
# Dicts are created with curly brackets and have keys and values
# Dicts are ORDERED, CHANGEABLE, DUPLICATES NOT ALLOWED

# Sample Dicts
capitals = {"USA":"Washington D.C", "India":"New Delhi", "China":"Beijing", "Russia":"Moscow"}

# Different methods that are available with Lists
# print(dir(capitals))
# Output of the above
# ['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

# For a detailed explanation of each of the Lists method
# print(help(capitals))
# Output of the above
'''
Help on dict object:

class dict(object)
 |  dict() -> new empty dictionary
 |  dict(mapping) -> new dictionary initialized from a mapping object's
 |      (key, value) pairs
 |  dict(iterable) -> new dictionary initialized as if via:
 |      d = {}
 |      for k, v in iterable:
 |          d[k] = v
 |  dict(**kwargs) -> new dictionary initialized with the name=value pairs
 |      in the keyword argument list.  For example:  dict(one=1, two=2)
 |
 |  Methods defined here:
 |
 |  __contains__(self, key, /)
 |      True if the dictionary has the specified key, else False.
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
 |  __getitem__(self, key, /)
 |      Return self[key].
 |
 |  __gt__(self, value, /)
 |      Return self>value.
 |
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  __ior__(self, value, /)
 |      Return self|=value.
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
 |  __ne__(self, value, /)
 |      Return self!=value.
 |
 |  __or__(self, value, /)
 |      Return self|value.
 |
 |  __repr__(self, /)
 |      Return repr(self).
 |
 |  __reversed__(self, /)
 |      Return a reverse iterator over the dict keys.
 |
 |  __ror__(self, value, /)
 |      Return value|self.
 |
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |
 |  __sizeof__(self, /)
 |      Return the size of the dict in memory, in bytes.
 |
 |  clear(self, /)
 |      Remove all items from the dict.
 |
 |  copy(self, /)
 |      Return a shallow copy of the dict.
 |
 |  get(self, key, default=None, /)
 |      Return the value for key if key is in the dictionary, else default.
 |
 |  items(self, /)
 |      Return a set-like object providing a view on the dict's items.
 |
 |  keys(self, /)
 |      Return a set-like object providing a view on the dict's keys.
 |
 |  pop(self, key, default=<unrepresentable>, /)
 |      D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
 |
 |      If the key is not found, return the default if given; otherwise,
 |      raise a KeyError.
 |
 |  popitem(self, /)
 |      Remove and return a (key, value) pair as a 2-tuple.
 |
 |      Pairs are returned in LIFO (last-in, first-out) order.
 |      Raises KeyError if the dict is empty.
 |
 |  setdefault(self, key, default=None, /)
 |      Insert key with a value of default if key is not in the dictionary.
 |
 |      Return the value for key if key is in the dictionary, else default.
 |
 |  update(...)
 |      D.update([E, ]**F) -> None.  Update D from mapping/iterable E and F.
 |      If E is present and has a .keys() method, then does:  for k in E.keys(): D[k] = E[k]
 |      If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
 |      In either case, this is followed by: for k in F:  D[k] = F[k]
 |
 |  values(self, /)
 |      Return an object providing a view on the dict's values.
 |
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |
 |  __class_getitem__(object, /)
 |      See PEP 585
 |
 |  fromkeys(iterable, value=None, /)
 |      Create a new dictionary with keys from iterable and values set to value.
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

# capitals = {"USA":"Washington D.C", "India":"New Delhi", "China":"Beijing", "Russia":"Moscow"}
# Accessing elements in the dicts
print(capitals.get("USA")) # Washington D.C
print(capitals.keys()) # dict_keys(['USA', 'India', 'China', 'Russia'])
print(capitals.values()) # dict_values(['Washington D.C', 'New Delhi', 'Beijing', 'Moscow'])

# Lets try some of the Dicts methods
# Length of the Dicts
print(len(capitals))

# using the 'in' method, spits out True or False, Depends of whether the string case-sensitive
print("USA" in capitals) # woruld return True
print("usa" in capitals) # woruld return False

# Update the value in dicts
capitals.update({"Germany":"Berlin"})
print(capitals) # {'USA': 'Washington D.C', 'India': 'New Delhi', 'China': 'Beijing', 'Russia': 'Moscow', 'Germany': 'Berlin'}


# Pop the values using 'pop' method. pop method removes the specified value in the dicts
print(capitals.pop("China"))
# china: Beijing will be popped from the dict {'USA': 'Washington D.C', 'India': 'New Delhi', 'China': 'Beijing', 'Russia': 'Moscow', 'Germany': 'Berlin'}

# Popitem the values using 'popitem' method. popitem method removes the last key/value in the dicts
print(capitals.popitem())
# ('Germany', 'Berlin') will be popped from the dict {'USA': 'Washington D.C', 'India': 'New Delhi', 'Russia': 'Moscow', 'Germany': 'Berlin'}
print(capitals)

# items returns the key value in 2d list tuples. 
print(capitals.items())
# dict_items([('USA', 'Washington D.C'), ('India', 'New Delhi'), ('Russia', 'Moscow')])

# for loops using items method
for key, value in capitals.items():
    print(f'{key}: {value}')
    
# USA: Washington D.C
# India: New Delhi
# Russia: Moscow

# Clear the dicts using 'clear' method. Clear method clears all the values in dicts.
capitals.clear()
print(capitals)
# {} Cleared the values in the dicts