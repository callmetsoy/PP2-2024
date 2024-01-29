# First example
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist) # we can replace element that has index 1 to blackcurrant
# Second example 
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist) # also we can use range for changing elements of list 
# Third example 
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist) # we can replace one element of list to two elements, so we change length of list 
# Fourth example
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist) # also we can replace two elements of list to one 
# Fifth example 
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist) # use function insert to add watermelon in place according to index , insert(index, element)
