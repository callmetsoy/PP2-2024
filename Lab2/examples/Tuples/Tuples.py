"""
A tuple is a collection which is ordered and unchangeable and allow duplicate value.
Tuples are written with round brackets.
"""
# First example
thistuple = ("apple", "banana", "cherry")
print(thistuple)
# Second example
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple) # allow dupllicate 
# Third example
thistuple = ("apple", "banana", "cherry")
print(len(thistuple)) # use function len() to print length of tuple
# Fourth example
thistuple = ("apple",)
print(type(thistuple)) # type tuple
#NOT a tuple
thistuple = ("apple")
print(type(thistuple)) # type str
# Fifth example
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
# Sixth example
tuple1 = ("abc", 34, True, 40, "male") # all types of data 
# Seventh example
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))
# Eight example
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

