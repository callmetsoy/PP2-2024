"""
A dictionary is a collection which is ordered*, changeable and do not allow duplic
Dictionaries are written with curly brackets, and have keys and values
"""
# First example
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
# Second example
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
# Third example
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict) # dict dont allow duplicates
# Fourth example
print(len(thisdict)) 
# Fifth example
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
# Sixth example
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))
# Seventh example
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)