nums = [5]
target = 5
l=0
t=0
mid=0
r=len(nums)-1
nums.sort()
while l<=r:
    mid=int((l+r)/2)
    if target<nums[mid]:
        r=mid-1
    if target>nums[mid]:
        l=mid+1
    if target==nums[mid]:
        t=1
        break
if t==1:
    print(mid)
else:
    print(-1)