strs=["flower","flow","flight"]
if not strs:
    print ("")
n = sorted(strs)
for i in range(len(n[0])):
    for string in (n[1:]):
        if (string[i] != n[0][i]) or (i >= len(string)):
            print (n[0][:i])