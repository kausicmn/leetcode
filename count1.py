n=10
if n==0:
    print(0)
primes=[True for i in range(n+1)]
p=2
count=0
while p*p<=n:
    if primes[p] is True:
        for i in range(p*2,n+1,p):
            primes[i]=False
    p+=1
primes[0],primes[1]=False,False
for t in range(n):
    if primes[t] is True:
        count+=1
print(count)
