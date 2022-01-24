def x():
    a="qwertyuiop"
    
    b="asdfghjkl"
    c="zxcvbnm"
    words =["asdfghjkl","qwertyuiop","zxcvbnm"]

    j=0
    i=0
    t=[]
    v=[]
    s=1
    p=0
    n=0
    while i<len(words):
        while j<len(words[i]):
            if words[i][p].casefold() in a:
                t.append(words[i][p])
                p=p+1
                j=j+1
                if len(t)==len(words[i]):
                    v.append(words[i])
                    t=[]
                    p=0

            else:
                a=b
                p=0
                t=[]
                s=s+1

                if(s==3):
                    t=[]
                    a=c
                    p=0
                if(s==4):
                    t=[]
                    p=0

                    break
        i=i+1
        j=0
        s=1
        a="qwertyuiop"

    return(v)

print(x())









