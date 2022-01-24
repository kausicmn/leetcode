n=5
n=n+1
if n==1:
    print(n)
else:
    a=0
    b=1
    c=0
    for i in range(1,n):
        c=a+b
        a=b
        b=c
    print(c)
