n = 4
k=2
for i in range(2,n+1):
    t=bin(i)
    z=t.replace("0b","")
    if len(z)>1:
        for j in range(1,len(z)):
            h=z[j-1]
            b=z[j]

            if z[j-1]=="1" and z[j]=="1":
                break
            if j==len(z)-1:
                k=k+1
print(k)

