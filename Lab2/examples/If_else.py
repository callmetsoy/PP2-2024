# First example
a = 33
b = 200
if b > a:
  print("b is greater than a")
# Second example
a = 33
b = 200
if b > a:
print("b is greater than a") # you will get an error
# Third example
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
# Fourth example
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
# Fifth example
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
# Sixth example
if a > b: print("a is greater than b")
# Seventh example
a = 2
b = 330
print("A") if a > b else print("B")
# Eigth example
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
# Nineth example
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
# Tenth example
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
# Eleventh example
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")
# Twelveth example 
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
# Thirteen example
a = 33
b = 200

if b > a:
  pass