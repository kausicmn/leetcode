nums=[5,0,7,6]


for i in range(len(nums)):
    if nums[i]==0:
        nums.remove(nums[i])
        nums.append(0)
        #nums[i+1]=nums[i]
print(nums)
nums=[5,0,7,6]
non_zero_pointer = zero_pointer = 0

while non_zero_pointer < len(nums):
    if nums[non_zero_pointer] != 0:
        nums[non_zero_pointer], nums[zero_pointer] = nums[zero_pointer], nums[non_zero_pointer] #swap nodes
        non_zero_pointer += 1
        zero_pointer += 1
    else:
        non_zero_pointer += 1
print(nums)