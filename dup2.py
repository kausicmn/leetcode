nums=[0,1,2,2,3,0,4,2]
val=2
for i in range(len(nums)-1,-1,-1):
    if nums[i]==val:
        nums.remove(nums[i])
print(nums)
print(len(nums))
