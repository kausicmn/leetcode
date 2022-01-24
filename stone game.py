piles = [5,3,4,5]
a=0
b=0
for i in range(0,len(piles)):
    left=0
    right=len(piles)-1
    if i%2==0:
        if piles[left]>=piles[right]:
            a=a+piles[left]
            piles.remove(piles[left])
        else:
            a=a+piles[right]
            piles.remove(piles[right])
    else:
        if piles[left]<piles[right]:
            b=b+piles[left]
            piles.remove(piles[left])
b=b+piles[0]

if a>b:
    print(True)
else:
    print(False)
print(piles)
print(a)
print(b)


