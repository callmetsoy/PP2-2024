from math import *
 
n = int(input("Input number of sides: "))
a = int(input("Input the length of a side: "))

Area = (a**2 * n) / (4*tan(pi/n))
print(Area)