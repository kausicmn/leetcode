s = "race a car"
t=""

for i in s:
    if i.isalnum():
        t=t+i

t=t.casefold()


if t==t[::-1]:
    print(True)
else:
    print(False)

