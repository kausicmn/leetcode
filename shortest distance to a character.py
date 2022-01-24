s = "loveleetcode"
c = "e"

l=[]
for i in range(0,len(s)):
    if s[i]==c:
        l.append(i)
d=[]
for j in range(0,len(s)):
    d.append(min(abs(j-x)for x in l))
print(d)
