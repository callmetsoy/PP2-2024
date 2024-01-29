# First example
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
# Second example
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)
# Both and will exclude any duplicate items.union()update()
# Third example
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x) # the method will keep only the items that are present in both sets.intersection_update()
# Fourth example
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z) # The method will return a new set, that only contains the items that are present in both sets.intersection()
# Fifth example
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x) # The method will keep only the elements that are NOT present in both sets.symmetric_difference_update()
# Sixth example
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z) # The method will return a new set, that contains only the elements that are NOT present in both sets.symmetric_difference()
# Seventh example
x = {"apple", "banana", "cherry", True}
y = {"google", 1, "apple", 2}
z = x.symmetric_difference(y)
print(z) # 1 and True are equal
