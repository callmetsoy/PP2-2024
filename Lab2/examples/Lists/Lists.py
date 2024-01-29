""" 
List items are ordered, changeable, and allow duplicate values
Lists are created using square brackets
"""
# First example 
mylist = ["apple", "banana", "cherry"]
# Second example 
thislist = ["apple", "banana", "cherry"]
print(thislist)
# Third example 
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
# Fourth example
thislist = ["apple", "banana", "cherry"]
print(len(thislist)) #print 3 due to length of thislist equal to 3 len()
# Fifth example 
list1 = ["apple", "banana", "cherry"] # str
list2 = [1, 5, 7, 9, 3] # int 
list3 = [True, False, False] # bool
# Sixth example 
list1 = ["abc", 34, True, 40, "male"] # list can contain different data types
# Seventh example 
thislist = list(("apple", "banana", "cherry")) #  use the list() constructor when creating a new list. use the double round - brackets
print(thislist)
