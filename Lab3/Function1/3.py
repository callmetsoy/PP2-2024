def func(numheads, numlegs):
    x = (numheads * 4 - numlegs) / 2
    print("Chickens:", x, "Rabbits:", numheads - x)
func(int(input("numheads:")), int(input("numlegs:")))
    
    
