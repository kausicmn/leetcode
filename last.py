s="Hello world"
k=""
u=len(s)
c=0
l=[]
if len(s)==0:
    print(0)

if len(s)>0:
    for i in range(len(s)-1,-1,-1):
        if s[i]!=" ":
            break
        else:
            c=c+1
    for i in range(0,u-c):
        l.append(s[i])
    s=l

    for i in range(len(s)-1,-1,-1):
        if s[i]==" " :
            break
        else:
            k=k+s[i]
print(k)


print(len(k))