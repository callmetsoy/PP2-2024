def has_007(nums):
    for i in range(len(nums)):
        if i + 2 != len(nums):
            if nums[i] == 0 and nums[i + 1] == 0 and  nums[i + 2] == 7:
                return True
    return False



print(has_007([1, 2, 4, 0, 0, 7, 5]))
print(has_007([1, 0, 2, 4, 0, 5, 7]))