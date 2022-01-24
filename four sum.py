nums = [2,2,2,2,2]
target = 8
b=[]
nums.sort()
for i in range(0,len(nums)):
    for j in range(i+1,len(nums)):
        left=j+1
        right=len(nums)-1
        while left<right:
            result=nums[i]+nums[j]+nums[left]+nums[right]
            if result>target:
                right-=1
            if result<target:
                left=left+1
            if result==target:
                if [nums[i],nums[j],nums[left],nums[right]] not in b:
                    b.append([nums[i],nums[j],nums[left],nums[right]])
                left=left+1
                right=right-1


print(b)