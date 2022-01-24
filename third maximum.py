nums = [2,2,3,1]
if len(nums)>=3:
    nums=list(set(nums))
    if len(nums)>=3:
        nums.sort(reverse=True)
        print(nums[2])
    else:
        print(max(nums))

else:
    print(max(nums))