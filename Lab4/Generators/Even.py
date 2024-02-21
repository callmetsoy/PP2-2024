def even(n):
    for i in range(0, n + 1):
        if i % 2 == 0:
            yield i
nums = even(int(input()))
for i in nums:
    print(i)