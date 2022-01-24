nums = [1,2,3,4,4]
nums.sort()
for i in range(0,len(nums)-1):
        if nums[i]==nums[i+1]:
            print(True)
            break
else:
    print(False)
def x():
    seen = set()
    for i in nums:
        if i in seen:
            return(True)

        seen.add(i)
    return(False)
print(x())
