# First example
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
# Second example
x = thisdict.get("model") # use get to get value of the model key

# Third example
x = thisdict.keys() # get a list of the keys
# Fourth example
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change
"""print only keys""" 
# Fifth example
x = thisdict.values() # Get a list of the values
# Sixth example
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change
# Seventh example
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["color"] = "red"

print(x) #after the change
"""print only value""" 
# Eighth example
x = thisdict.items() # Get a list of the key:value pairs
# Nineth example
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["year"] = 2020

print(x) #after the change
# Tenth example
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["color"] = "red"

print(x) #after the change 
"""print only pair""" 

# Eleventh example
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
