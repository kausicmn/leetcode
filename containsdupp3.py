def f():
    nums = [1,0,1,1]
    k=1
    if len(nums)==len(list(set(nums))):
        return False
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]==nums[j] and abs(i-j)<=k:
                return True
    return False
print(f())