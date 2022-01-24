flowerbed = [1,0]
n=0
k=0
if len(flowerbed)>2:
    if flowerbed[0]==0 and flowerbed[1]==0:
        k=k+1
        flowerbed.pop(0)
        flowerbed.insert(0,1)
    for i in range(1,len(flowerbed)-1):
        t=flowerbed[i-1]
        f=flowerbed[i+1]
        if flowerbed[i]==0 and flowerbed[i-1]==flowerbed[i] and flowerbed[i]==flowerbed[i+1]:
            flowerbed.pop(i)
            flowerbed.insert(i,1)
            k=k+1
    if flowerbed[len(flowerbed)-1]==0 and flowerbed[len(flowerbed)-2]==0:
        k=k+1
    if k>=n:
        print(True)
    else:
        print(False)
if len(flowerbed)==1:
    if(flowerbed[0]==0 and n==1) or (flowerbed[0]>=0 and n==0):
        print(True)
    else:
        print(False)
if len(flowerbed)==2:
    for i in flowerbed:
        if (i==0 and flowerbed.count(i)==2 and n==1)or(i==1 and flowerbed.count(i)<=2 and n==0):
            print(True)
            break
        else:
            print(False)
            break

