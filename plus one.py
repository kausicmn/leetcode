digits=[9,9]
t=digits
f=0
u=len(digits)-1
c=0

for i in range(len(digits)-1,-1,-1):
    if(digits[i])==9:
        digits.remove(digits[i])

        digits.append(0)
        c=c+1
digits[len(digits)-1-c]=digits[len(digits)-1-c]+1

if len(digits)==1 and digits[u]==1:
    digits.append(0)


if len(digits)>2 and digits[u]==1:
    f=digits.reverse()
    f=digits




print(digits)
