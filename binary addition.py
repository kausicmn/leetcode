a = "1010"
b = "1011"
j=0
h=0
a=list(a)
b=list(b)
sum=0
sum1=0
for i in range(len(a)-1,-1,-1):
    if a[i]=="1":
        a[i]=2**j
        j=j+1
    else:

        j=j+1
print(a)

for i in range(0,len(a)):
    if a[i]!="0":
        sum=sum+a[i]

print(sum)
for i in range(len(b)-1,-1,-1):
    if b[i]=="1":
        b[i]=2**h
        h=h+1
    else:

        h=h+1
print(b)

for i in range(0,len(b)):
    if b[i]!="0":
        sum1=sum1+b[i]

print(sum1)
v=sum+sum1
print(v)
t=bin(v)

print(t.replace("0b",""))
