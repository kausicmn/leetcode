# def d():
#     nums=[0,0,1,1,1,2,2,3,3,4]
#
#     l=[]
#     r=0
#     for i in nums:
#         if i not in l:
#             l.append(i)
#
#         else:
#             r=r+1
#     for i in range(r):
#         l.append(("_"))
#
#     k=0
#     for i in l:
#         if i!="_":
#             k+=1
#
#     return(k,l)
#
#
#
# print(d())

def dp():
    nums=[1,1,2]
    count=0
    j=1
    for i in range(len(nums)-1):
        if nums[count]!=nums[i+1]:
            count=count+1
            nums.remove(nums[i])
        else:

            j=j+1







    return(len(nums))

print(dp())
# nums=[1,1,1]
#
# i=0
# j=1
# n=len(nums)
# while j<n:
#     if nums[i]==nums[j]:
#         nums.pop(j)
#     else:
#         i+=1
#         j+=1
#     n=len(nums)
# print(len(nums))

