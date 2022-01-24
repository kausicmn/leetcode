list1 =["Shogun","Piatti","Tapioca Express","Burger King","KFC"]
list2 =["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
l=[]
j=[]
u=[]
n=0
for i in list1:
    if i in list2 :
        t=list1.index(i)+list2.index(i)
        l.append(t)
        j.append(i)
for n in range(0,len(l)-1):
        if l[n]==l[n+1]:
            u.append(l[n])
            if n==len(l)-2:
                u.append(l[n+1])




if l!=u:
    k=l.index(min(l))
    print(j[k])
if l==u:
    print(j)
























