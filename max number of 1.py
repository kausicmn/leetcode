nums = [1,0,1,1,0,1]
k=list(set(nums))
c=0
max=0
for i in range(0,len(nums)):
    if nums[i]==1:
        c=c+1
        if max<c:
            max=c
    else:
        c=0
print(max)


