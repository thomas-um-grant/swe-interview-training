########################
######## Basics ########
########################

# A dictionary is a data structure that provides fast insertion, deletion, and lookup of key/value pairs.
# Under the hood, it's just a dynamic array of linked lists.
# The following are a dictionary's standard operations and their corresponding time complexities:
# Inserting a key/value pair: O(1) on average. O(n) worse case.
# Removing a key/value pair: O(1) on average. O(n) worse case.
# Looking up a key/value pair: O(1) on average. O(n) worse case.

# Operations:
list(d) # Return a list of all the keys used in the dictionary d.
len(d) # Return the number of items in the dictionary d.
d[key] # Return the item of d with key key. Raises a KeyError if key is not in the map.
d[key] = value # Set d[key] to value.
del d[key] # Remove d[key] from d. Raises a KeyError if key is not in the map.
key in d # Return True if d has a key key, else False.
key not in d # Equivalent to not key in d.
iter(d) # Return an iterator over the keys of the dictionary. This is a shortcut for iter(d.keys()).
clear() # Remove all items from the dictionary.
copy() # Return a shallow copy of the dictionary.
classmethod fromkeys(iterable[, value]) # Create a new dictionary with keys from iterable and values set to value.
 # fromkeys() is a class method that returns a new dictionary. value defaults to None. All of the values refer to just a single instance, so it generally doesn’t make sense for value to be a mutable object such as an empty list. To get distinct values, use a dict comprehension instead.
get(key[, default]) # Return the value for key if key is in the dictionary, else default. If default is not given, it defaults to None, so that this method never raises a KeyError.
items() # Return a new view of the dictionary’s items ((key, value) pairs). See the documentation of view objects.
keys() # Return a new view of the dictionary’s keys. See the documentation of view objects.
pop(key[, default]) # If key is in the dictionary, remove it and return its value, else return default. If default is not given and key is not in the dictionary, a KeyError is raised.
popitem() # Remove and return a (key, value) pair from the dictionary. Pairs are returned in LIFO order.
 # popitem() is useful to destructively iterate over a dictionary, as often used in set algorithms. Ifthe dictionary is empty, calling popitem() raises a KeyError.
 # LIFO order is now guaranteed. In prior versions, popitem() would return an arbitrary key/value pair.
reversed(d) # Return a reverse iterator over the keys of the dictionary. This is a shortcut for reversed(d.keys()).
setdefault(key[, default]) # If key is in the dictionary, return its value. If not, insert key with a value of default and return default. default defaults to None.
update([other]) # Update the dictionary with the key/value pairs from other, overwriting existing keys. Return None.
 # update() accepts either another dictionary object or an iterable of key/value pairs (as tuples or other iterables of length two). If keyword arguments are specified, the dictionary is then updated with those key/value pairs: d.update(red=1, blue=2).
values() # Return a new view of the dictionary’s values.
d | other # Create a new dictionary with the merged keys and values of d and other, which must both be dictionaries. The values of other take priority when d and other share keys.
d |= other # Update the dictionary d with keys and values from other, which may be either a mapping or an iterable of key/value pairs. The values of other take priority when d and other share keys.
len(dictview) # Return the number of entries in the dictionary.
iter(dictview) # Return an iterator over the keys, values or items (represented as tuples of (key, value)) in the dictionary.
 # Keys and values are iterated over in insertion order. This allows the creation of (value, key) pairs using zip(): pairs = zip(d.values(), d.keys()). Another way to create the same list is pairs = [(v, k) for (k, v) in d.items()].
 # Iterating views while adding or deleting entries in the dictionary may raise a RuntimeError or fail to iterate over all entries.
x in dictview # Return True if x is in the underlying dictionary’s keys, values or items (in the latter case, x should be a (key, value) tuple).
reversed(dictview) # Return a reverse iterator over the keys, values or items of the dictionary. The view will be iterated in reverse order of the insertion.
 # Dictionary views are now reversible.
dictview.mapping # Return a types.MappingProxyType that wraps the original dictionary to which the view refers.

########################
######### More #########
########################

# More info there: https://docs.python.org/3/library/stdtypes.html#dict


