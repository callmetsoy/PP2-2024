def square(n):
    for i in range(1, n + 1):
        yield i**2
nums = square(int(input()))
for i in nums:
    print(i)