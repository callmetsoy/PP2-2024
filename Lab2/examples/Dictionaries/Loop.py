# First example
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x) # Print all key names in the dictionary, one by one
# Second example
for x in thisdict:
  print(thisdict[x]) # Print all values in the dictionary, one by one
# Third example
for x in thisdict.values():
  print(x)
# Fourth example
for x in thisdict.keys():
  print(x)
# Fifth example
for x, y in thisdict.items():
  print(x, y) 