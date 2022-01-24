nums = [2,2,1,1,1,2,2]
s=list(set(nums))
n=len(nums)
t=0
for i in s:
    if nums.count(i)>n/2:
        t=i
print(t)