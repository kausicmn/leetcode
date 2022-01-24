s = "art"
indices = [1,0,2]
l=[]
i=0
for j in range(len(indices)):
        t=indices.index(i)
        l.append(s[t])
        i=i+1
print("".join(l))