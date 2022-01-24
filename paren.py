def d():
    dict={"(":")","[":"]","{":"}"}
    s="[{"
    k=[]
    if s=="":
        return(True)
    if len(s)<2:
        print(False)

    for i in s:
        if i in dict:
            k.append(i)

        else:
            if len(k)==0 or dict[k.pop()]!=i:
                return (False)
    if len(k)>0:
        return(False)
    return(True)
print(d())
