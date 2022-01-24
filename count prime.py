n=499979
count=0
for i in range(2,n):
    if i>1:
        for j in range(2,int(i/2)+1):
            if i%j==0:
                break
        else:
            count=count+1
print(count)


