dict={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"xyz"}
digits="2345"
l=[]
x=[]
s=[]
t=""
i=1
z=""
o=""

if len(digits)>=2:
    for j in dict[digits[i-1]]:
        for k in dict[digits[i]]:
                t=j+k
                l.append(t)
    if len(digits)>=3:
        for u in l:
            for n in dict[digits[i+1]]:
                z=u+n
                x.append(z)

    if len(digits)==4:
        for g in x:
            for q in dict[digits[i+2]]:
                o=g+q
                s.append(o)


if len(digits)==1:
    for j in dict[digits[0]]:
        l.append(j)
    print(l)
if len(digits)==0:
    print([])
if len(digits)==2:
    print(l)
if len(digits)==3:
    print(x)
if len(digits)==4:
    print(s)

