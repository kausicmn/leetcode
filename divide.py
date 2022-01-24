dividend=-2147483647
divide=-1
s=dividend/divide
if s>2**31-1:
    print(2**31-1)
else:
    print(int(s))