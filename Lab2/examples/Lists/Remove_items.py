# First example 
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist) # use function remove(element) to remove the element of list
# Second example 
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist) # if there are more than one item with the specified value, the remove() method removes the first occurance
# Third example
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist) # use function pop(index) to remove the specified index
# Fourth example 
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist) # if we use function pop() without index pop remove last item
# Fifth example 
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist) # use del to remove the specified index 
# Sixth example 
thislist = ["apple", "banana", "cherry"]
del thislist # without index del remove all list 
# Seventh example 
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist) # use function clear to empties the list