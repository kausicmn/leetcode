def happy(n):

    temp=0
    t=0

    while n!=0:
        t=n%10
        temp=temp+(t*t)
        n=n//10
    return(temp)

n=int(input())
r=n
while r!=1 and r!=4:
    r=happy(r)
if r==1:
    print(r)
else:
    print(r)