def s():
    nums = [0,2,1,-3]
    nums.sort()
    target = 1

    u=0
    left=1
    right=len(nums)-1
    result=nums[0]+nums[left]+nums[right]
    if target>=0:
        if target>result:
            t=target-result
        else:
            t=result-target
    else:
        t=target-result


    minn=t
    u=result
    if len(nums)==3:
        print(result)

    if len(nums)>3:
        for i in range(1,len(nums)):
                left=i+1
                right=len(nums)-1
                while left<right:
                    result=nums[i]+nums[left]+nums[right]
                    if target>0:
                        if target>result:
                            t=target-result
                        else:
                            t=result-target
                    if target<0:
                        t=target-result
                    if t<minn and target>=0:
                        minn=t
                        u=result
                    if t>minn and target<0:
                        minn=t
                        u=result
                    left+=1
                    right-=1


        return(u)
print(s())