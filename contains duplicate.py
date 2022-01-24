nums = [1,2,3,4,2]
nums.sort()
s=list(set(nums))
if s==nums:
    print(False)
else:
    for i in s:
        if nums.count(i)>=2:
            print(True)
            break


