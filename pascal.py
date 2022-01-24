def s(o):


        v=[1,1]
        t=0
        mid=len(v)//2
        n=3
        i=0
        k=len(o)

        for j in range(0,len(o)-1):

                t=o[j]+o[j+1]
                v.insert(mid,t)



        return(v)
n=5
i=1
a=[[1]]
z=[1,1]
a.append(z)


if(n>=3):
        while(i<=n-2):
                z=s(z)
                a.append(z)
                i=i+1
        print(a)


if(n==1):
        print([[1]])
if n==2:
        print(a)

