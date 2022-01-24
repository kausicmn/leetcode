def y():
    prices=[7,10,5,3,6,4]
    i=0
    j=1
    maxx=0
    while j<len(prices):
        if prices[i]<prices[j]:
            t=prices[j]-prices[i]
            if(maxx<t):
                maxx=t
        else:
            i=j
        j=j+1







    return(maxx)
print(y())