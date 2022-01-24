nums = [1,2,3,4]
l=[]
for i in range(0,len(nums),2):
        l.append([nums[i],nums[i+1]])
print(l)
n=0
for i in range(0,len(l)):
        n=n+min(l[i])
print(n)

