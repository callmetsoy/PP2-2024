def down(n):
    for i in range(n, -1, -1):
        yield i
nums = down(int(input()))
for i in nums:
    print(i)
