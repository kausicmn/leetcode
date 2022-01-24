
def j(strs):

    j=1
    i=0
    k=1
    l=[]
    count=0
    if len(strs[i])<len(strs[i+1]):
        strs[i],strs[i+1]=strs[i+1],strs[i]
    while len(strs[i])==1:
        if strs[i]==strs[i+1]:
            return(strs[i])

        else:
            return("")

    while True:


        if strs[i][:j]==strs[i+1][:k]:

            l.append(strs[i][j-1])

            j+=1
            k+=1

        else:
            j=j+1
            k=k+1
        count=len(strs[i])+1

        if count==j:
            break

    return(l)
strs=["abc","bcb"]
#print(len(strs))
s=[]
global t
global u
if strs!=[""*len(strs)] and len(strs)>1 and strs!=["",""*len(strs)]:
    t="".join(j(strs))
    u=t.split()
else:
    print(strs[0])

h=0
if len(strs)>2 and  len(u)>=1:
    for b in range(2,len(strs)):
        u.append(strs[b])
        h=j(u)

    print("".join(h))
else:
    print()






