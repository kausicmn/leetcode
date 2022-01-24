nums = [-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]
nums.sort()

a = nums[0]*nums[1]*nums[-1]
b=nums[-1]*nums[-2]*nums[-3]
print( max(a,b))


