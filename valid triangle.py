nums =[2,6,7,8,16,21]
nums.sort()
c=0
# for i in range(0,len(nums)):
#     for j in range(i+1,len(nums)):
#         for k in range(j+1,len(nums)):
#             if nums[i]+nums[j]>nums[k] and nums[j]+nums[k]>nums[i] and nums[k]+nums[i]>nums[j]:
#                 c=c+1
# print(c)

for i in range(2,len(nums)):
    left=0
    right=i-1
    while(left<right):
        if(nums[left]+nums[right]>nums[i]):
            c=c+(right-left)
            right=right-1
        else:
            left=left+1
print(c)
