nums=[-1,2,1,-4]
target=1
nums.sort()
minn=float("inf")
t=-1
for i in range(0,len(nums)):
    left=i+1
    right=len(nums)-1
    while left<right:
        result=nums[i]+nums[left]+nums[right]
        if result==target:
            print(target)
        if abs(result-target)< minn:
            minn=abs(result-target)
            t=result
        if result < target:
            left += 1
        else:
            right -= 1
print(t)