
def d(s):

    l=[]
    j=1
    n=len(s)
    while j<n:
        if s[j-1]==s[j]:
            j=j+2
        else:
            l.append(s[j-1])
            j=j+1
    if j==n:
        l.append(s[j-1])
    if j>n and len(l)==0: #aaaaaaaa
       l=[]

    return(l)


s=input()
s=list(s)
t=s
k=[]
u=0
while len(t)>2:
     t=d(t)
     u+=1
     if(u==5):
        for i in t:
            if i in t:
                k.append(i)
     if (k==t):
        print("".join(k))
        break


else:
    print("".join(t))





