matrix = [[1,2,3],[4,5,6]]
l=[]
k=[]
j=0
i=0
while j<len(matrix[0]):
    while i<len(matrix):
        l.append(matrix[i][j])
        i=i+1
    k.append(l)
    l=[]

    j=j+1
    i=0


print(k)


