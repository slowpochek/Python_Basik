
nums = [12, 3, 4, 10]
if len(nums) > 0:
    nums.insert(0 ,nums[-1] )
    nums.pop()
print(nums)