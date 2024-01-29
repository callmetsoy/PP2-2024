# First example
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset) # If the item to remove does not exist, remove() will raise an error.
# Second example
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset) # If the item to remove does not exist, discard() will NOT raise an error.
# Third example
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset) # Sets are unordered, so when using the pop() method, you do not know which item that gets removed.
# Fifth example
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)
# Sixth example
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)