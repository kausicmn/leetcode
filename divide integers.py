dividend=2147483647
divisor=1
t=0
u=0
if dividend <0 and dividend> -2147483647:
    t=-dividend
else:
    t=dividend
if divisor<0 and dividend> -2147483647:
    u=-divisor
else:
    u=divisor
if t>=0 and u>=0 or t>-2147483648:
    s=t//u

    if s<2**31-1 and s!=-2147483648:
        if dividend <0 and divisor<0:
            print(s)
        elif dividend <0 or divisor<0 :
            print(-s)
        elif dividend >0 or divisor>0:
            print(s)
    elif s>2**31-1  :
        print(2**31-1)
    if s<2**31-1 and s==-2147483648:
        print(s)
# a=-2147483648
# b=-1
# c=a%b
# print(c)
# t=2**31-1
# print(t)