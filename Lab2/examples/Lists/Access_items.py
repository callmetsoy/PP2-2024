# First example 
thislist = ["apple", "banana", "cherry"]
print(thislist[1]) # index start from 0, so it will print second element of list
# Second example
thislist = ["apple", "banana", "cherry"]
print(thislist[-1]) # negative index means that it will print last element of list
# Third example
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) # index 5 not included 
# Fourth example 
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4]) # the search start from the beginning to third element of list due to index 4 not included 
# Fifth example 
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:]) # the search start from index 2 to end of list, but index 0 and index 1 not included
# Sixth example 
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1]) # the search start from orange and mango, but mango not included due to it is end of range
# Seventh example 
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list") # we use operator "in" to check is there apple in list or not


