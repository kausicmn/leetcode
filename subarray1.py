nums = [-2,1,-3,4,-1,2,1,-5,4]

total=sum=nums[0]

for i in range(1,len(nums)):
    total=max(nums[i],total+nums[i])
    sum=max(total,sum)
print(sum)
