numbers = [2,3,4]
target=6
l=[]
s=0
e=len(numbers)-1

while s<e:
    if numbers[s]+numbers[e]<target:
        s=s+1
    if numbers[s]+numbers[e]>target:
        e=e-1
    if numbers[s]+numbers[e]==target:
        print([s+1,e+1])
        break

