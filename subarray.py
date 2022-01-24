nums = [5,4,-1,7,8]
sums=0
l=[]
largest=min(nums)
for i in range(0,len(nums)):
    for j in range(i,len(nums)):
        for k in range(i,j+1):

            l.append(nums[k])
            sums=sum(l)
        if largest<sums:
            largest=sums
            sums=0
            l=[]
        else:
            sums=0
            l=[]

            #if largest<sums:
            #    largest=sums




print(largest)