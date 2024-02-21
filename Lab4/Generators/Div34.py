def div(n):
    for i in range(0, n + 1):
        if i % 12 == 0:
            yield i
nums = div(int(input()))
for i in nums:
    print(i)