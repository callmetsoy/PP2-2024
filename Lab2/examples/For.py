# First example
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
# Second example 
for x in "banana":
  print(x) 
# Third example 
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break # use break to stop loop for
# Fourth example 
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
# Fifth example
for x in range(6):
  print(x)
# Sixth example
for x in range(2, 6):
  print(x)
# Seventh example 
for x in range(2, 30, 3):
  print(x)
# Eight example
for x in range(6):
  print(x)
else:
  print("Finally finished!")
# Nineth example 
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
# Tenth example
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
# Eleventh example
for x in [0, 1, 2]:
  pass # having an empty for loop like this, would raise an error without the pass statement
