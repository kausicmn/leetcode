l=["(",")","[","]","{","}",""]
s="{ { } [ ] [ [ [ ] ] ] }"
s=list(s)

k=len(s)
i=0
j=0
o=0
t=len(s)

while i<t:
    j=l.index(s[o])
    if s[o] in l:
        if l[j+1] in s[:]:

            s.remove(l[j+1])
            s.remove(s[o])

    if(s==[]):
        break
    i=i+1




if(s==[]):
    print(True)
else:
    print(False)
