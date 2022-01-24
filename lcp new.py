def k():
    strs=["flower","flow","flight"]

    if len(strs)==0:
        print("")
    if len(strs)==1:
        print(strs[0])
    min=len(strs[0])
    for i in range(len(strs)):
        if min>len(strs[i]):
            min=len(strs[i])

#print(min)
    j=0

    l=""
    while j<min:
        char=strs[0][j]
        for i in range(1,len(strs)):
            if char!=strs[i][j]:
                return(l)

        l=l+char
        j=j+1
    return(l)

print(k())



