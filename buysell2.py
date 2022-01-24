def y():
    prices=[1,2,3,4,5]
    i=0
    j=1
    maxx=0
    while j<len(prices):
        if prices[i]<prices[j]:
            maxx+=prices[j]-prices[i]
        i=i+1
        j=j+1











    return(maxx)
print(y())