nums = [1,1]
k=set(nums)
n=len(nums)
l=[]
for i in range(1,n+1):
    if i not in k:
        l.append(i)
print(l)