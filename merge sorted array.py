nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

nums1=nums1[0:m]
nums2=nums2[0:n]

for i in range(0,len(nums2)):
    nums1.append(nums2[i])

for i in range(0,len(nums1)):
    for j in range(i+1,len(nums1)):
        if nums1[i]>nums1[j]:
            temp=nums1[i]
            nums1[i]=nums1[j]
            nums1[j]=temp
print(nums1)
