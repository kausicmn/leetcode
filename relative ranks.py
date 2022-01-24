score = [5,4,3,2,1]
t=sorted(score,reverse=True)
l=[]
for i in score:
       u=t.index(i)
       if u==0:
           l.append("Gold Medal")
       if u==1:
            l.append("Silver Medal")
       if u==2:
            l.append("Bronze Medal")
       if u>2:
            l.append(str(u+1))
print(l)



