# First example
print(10 > 9)
print(10 == 9)
print(10 < 9)

# Second example
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
  
# Third example
print(bool("Hello"))
print(bool(15))

# Fourth example
x = "Hello"
y = 15

print(bool(x))
print(bool(y))

# Fifth example return true
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

# Sixth example return false
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

# Seventh example __len__
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

# Eighth example 
def myFunction() :
  return True

print(myFunction())

# Nineth example
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

# tenth example isinstance is function that check x is int or not if not print false 
x = 200
print(isinstance(x, int))