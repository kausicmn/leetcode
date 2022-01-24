nums=[5,7,7,8,8,10]
target=11
s=list(set(nums))
l=[]
k=0
for i in range(0,len(nums)):
    if nums[i]==target:
        l.append(i)
    else:
        k=k+1
if k==len(nums):
    print([-1,-1])
else:
    print([min(l),max(l)])

