words=["cool","lock","cook"]
u=1
i=0
j=0
l=[]
while i<(len(words[0])):
    while u<len(words):
        if words[0][i] in words[u]:
                j=j+1
        if j==len(words)-1:
            l.append(words[0][i])
        u=u+1
    i=i+1
    u=1
    j=0
print(l)








