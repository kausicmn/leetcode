nums = [1,2,2,3,1]
freq = {}
max_freq = 0
first_occurance = {}
l = len(nums)

for i in range(0, l):
    if nums[i] not in freq:
        freq[nums[i]] = 1
        first_occurance[nums[i]] = i
    else:
        freq[nums[i]]+=1

    if freq[nums[i]]>max_freq:
        max_freq = freq[nums[i]]
        min_sub_length = i - first_occurance[nums[i]]+1
    elif freq[nums[i]]==max_freq:
        min_sub_length = min(min_sub_length, i - first_occurance[nums[i]]+1)

print( min_sub_length)