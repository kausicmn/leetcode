



# for i in range(1,n):
#     if nums[i]!=nums[i-1]:
#         nums[j]=nums[i]
#         j=j+1
# print(j)
nums=[1,1,2]
n=len(nums)
j=1
i=0
while j<n:
    if nums[i] == nums[j]:
        nums.remove(nums[j])

    else:
        i=i+1
        j=j+1
    n=len(nums)
print(n)
print(nums)










