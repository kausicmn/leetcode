nums =[100,1,11,1,120,111,123,1,-1,-100]
c=1
l=[]
j=0

for i in range(1,len(nums)):

    if nums[i]>nums[i-1]:
        l.append(nums[i])

    else:
        t=nums[i-1]
        for j in range(i-1,len(nums)) :
            if nums[j]>t:
                l.append(nums[j])
                break
        if i-1==len(l):
            for s in range(0,i):
                if nums[s]>t:
                    l.append(nums[j])
                    break



else:
    if len(l)!=len(nums):
        if nums[len(nums)-1]!=max(nums):
            nums.insert(0,nums[len(nums)-1])
            for k in range(1,len(nums)) :
                if nums[k]>nums[0]:
                    l.append(nums[k])
                    break
        else:
            l.append(-1)




print(l)