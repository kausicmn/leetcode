nums = [1,1,1,1,1,10000,10000,10000,10000,10000]
target = 1
start = 9
l=[]

for i in range(0,len(nums)):
    if nums[i]==target:
        t=abs(i-start)
        l.append(t)
print(min(l))