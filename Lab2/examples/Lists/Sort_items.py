# First example 
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist) 
# Second example 
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
# Third example 
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
# Fourth example 
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)
# Fifth example 
def myfunc(n):
  return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist) # sort how close numbers to 50
# Sixth example 
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist) # By default the method is case sensitive, resulting in all capital letters being sorted before lower case letters
# Seventh example 
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist) # we can use function str to change capital letters to small and sort without errors
# Eigth example 
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist) # use reverse to reverve order of list
