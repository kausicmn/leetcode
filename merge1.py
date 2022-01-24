nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
k=len(nums1)

for i in range(len(nums1)-1,m-1,-1):
    nums1.remove(nums1[i])
for i in range(0,n):
    nums1.append(nums2[i])
nums1.sort()


print(nums1)