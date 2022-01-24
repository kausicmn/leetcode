nums = [3,1,2]
if len(nums)==1:
    print(0)
if len(nums)==2:
    if nums[1]>nums[0]:
        print(1)
    else:
        print(0)
if len(nums)>2:
    t=0
    for i in range(1,len(nums)-1):
        if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
            t=1
            print(i)
            break
    if t==0 and nums[len(nums)-1]<nums[len(nums)-2]:
        print(0)
    if t==0 and nums[len(nums)-1]>nums[len(nums)-2]:
        print(len(nums)-1)

