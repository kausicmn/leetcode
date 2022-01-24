def f():
    nums = [1,2,3,1]
    k = 3
    t=-1

    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]==nums[j]:
                if abs(i-j)<=k:
                    t=1
                    break
            else:
                t=0
        if t==1:
            break
    if t==0:
        return(False)
    if t==1:
        return(True)

print(f())


