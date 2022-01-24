nums =[1,2,3,4,3]
l=[]
for i in range(0,len(nums)):
    for j in range(i+1,len(nums)):
        if nums[j]>nums[i]:
            l.append(nums[j])
            break
    else:
        t=nums[i]
        for k in range(0,i):
            if nums[k]>t:
                l.append(nums[k])
                break
        else:
            if len(l)!=len(nums):
                l.append(-1)



print(l)