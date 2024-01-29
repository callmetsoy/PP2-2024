# First example
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist) # we use function append, it adds element in end of list 
# Second example 
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist) # we use function insert to add elements in place according to index
# Third example 
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist) # we use function extend to unite lists and make one, extend(list) 
# Fourth example 
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist) # function extend can unite not only list and list, also we can unite list and (sets or tuples or dict)