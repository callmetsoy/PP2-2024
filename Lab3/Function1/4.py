def prime(n):
    for x in range(2, n):
        if n % x == 0:
            return False
    return True        

def filter(func, nums):
    rsl = []
    for x in nums:
        if func(x):
            rsl.append(x)
    return rsl

numbers = [1, 6, 7, 9, 11, 17]
print(filter(prime, numbers))
