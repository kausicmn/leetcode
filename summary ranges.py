nums =  [1,2]
if len(nums)==0:
    print(nums)
if len(nums)==1:
    print([str(nums[0])])
if len(nums)>1:
    l=nums[0]
    r=nums[len(nums)-1]
    s=[]
    j=0
    while j<len(nums):
        for i in range(l,r+1):
            if i not in nums:
                if l==i-1:
                    s.append(str(l))
                else:
                    s.append(str(l)+"->"+str(i-1))
                break
        if i!=nums[len(nums)-1]:
            u=nums.index(i-1)
            l=nums[u+1]
            j=u+1
        else:
            if l!=r:
                s.append(str(l)+"->"+str(r))
            else:
                s.append(str(l))
            j=len(nums)
            break
    print(s)

