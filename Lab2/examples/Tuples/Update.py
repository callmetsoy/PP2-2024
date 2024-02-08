# First example
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x) # convert tuple into a list to replace element 
# Second example
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y) # convert tuple into a list and add element by using append
# Third example
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple) 
# Fourth example
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
# Fifth example
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists
