def happy(n):

    temp=0
    t=0

    while n!=0:
        t=n%10
        temp=temp+(t*t)
        n=n//10
    return(temp)
s=0
j=0
n=int(input())
while True:
    if happy(n)==1:
        print(True)
        break
    n=happy(n)
    if n<10 and n!=7:
        print(False)
        break























