haystack ="helkohello"
needle ="ll"
if needle == "":
    print (0)
elif needle in haystack:
    print (haystack.index(needle))
else:
    print (-1)