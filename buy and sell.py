prices = [2,4,1]

t=min(prices)
u=prices.index(t)
f=prices[u+1:]

max=0
x=0
for j in f:
    if j-t>=t:
        x=j-t
        if max<x:
            max=x



print(max)