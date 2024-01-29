# First example 
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x) # you can loop through the list items by using a loop for
# Second example 
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i]) # You can also loop through the list items by referring to their index number. Use the and functions to create a suitable iterable.range()len()
# Third example 
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1 # use loop while 
# Fourth example
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist] 