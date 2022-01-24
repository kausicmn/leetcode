l = []
digits=[9,9,9,9]
for i in digits:
    l.append(str(i))
result = str(("".join(l)))
result=int(result)+1
result=str(result)
l.clear()
for i in result:
    l.append(int(i))
print(l)