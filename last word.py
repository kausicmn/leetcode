s="b a  "
k=""
if len(s)==0:
    print(0)
l=[]
s=list(s)
u=len(s)-1
c=0
if len(s)==3 and s[u]==" ":
    for i in range(0,u):
        l.append(s[i])
        s=l


if(s[u])==" ":
    for i in range(len(s)-1,-1,-1):
        if s[i]!=" ":
            break
        elif s[i]==" ":
            c=c+1


    for i in range(0,c):
        l.append(s[i])
        s=l
print(s)
if len(s)>0:

    for i in range(len(s)-1,-1,-1):

        if s[i]==" " :
            break
        else:
            k=k+s[i]
print(k)


print(len(k))


