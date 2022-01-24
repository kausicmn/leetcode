haystack ="mississippi"
needle ="issip"
if len(needle)==0 :
    print(0)
if len(haystack)==0 and len(needle)>=1:
    print(-1)
haystack=list(haystack)
needle=list(needle)
t=0
i=0
j=0
if len(needle)>0 and len(haystack)>0 and len(haystack)>=len(needle):

  while i<len(needle):
        if needle[i]==haystack[j]:
            i=i+1
            j=j+1
            if j==len(haystack):
                break


        else:
            j=j+1
            i=0
            if j==len(haystack):
                j=-1
                i=0
                break
if len(needle)>0 and len(haystack)>0 and len(haystack)>=len(needle):
    print(j-i)
if len(haystack)<len(needle):
    print(-1)



