nums=[9,6,4,2,3,5,7,0,1]
n=len(nums)
k=min(nums)
l=max(nums)
if 0 not in nums:
    print(0)
for i in range(k,n+1):
    if i not in nums:
        print(i)
