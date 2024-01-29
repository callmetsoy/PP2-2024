"""
Set items are unordered, unchangeable, and do not allow duplicate values.
Sets are written with curly brackets. 
"""
# First example
thisset = {"apple", "banana", "cherry"}
print(thisset) # ignore order
# Second example
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset) # ignore duplicates 
# Third example
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset) # True and 1 is considered the same value
# Fourth example
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset) # False and 0 is considered the same value
# Fifth example
thisset = {"apple", "banana", "cherry"}
print(len(thisset))
# Sixth example
set1 = {"apple", "banana", "cherry"} # string 
set2 = {1, 5, 7, 9, 3} # int
set3 = {True, False, False} # boolean
# Seventh example
set1 = {"abc", 34, True, 40, "male"} # all data types
# Eighth example
myset = {"apple", "banana", "cherry"}
print(type(myset))
# Nineth example
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset) 
