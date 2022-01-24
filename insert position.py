nums = [1,3,5,6]
target = 5

nums.append(target)
for i in range(0,len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]>nums[j]:
            temp=nums[i]
            nums[i]=nums[j]
            nums[j]=temp
print(nums.index(target))
print(nums)