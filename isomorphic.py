s = "badc"
t = "baba
l=[]
x=[]
# for i in range(len(s)):
#     if t[i] not in t[:i] and s[i] not in s[:i]:
#         l.append(s[i])
#         x.append(t[i])

k=1
i=0
d={}
d.update({s[i]:t[i]})
for i in range(1,len(s)):
    if t[i] not in t[:i] and s[i] not in s[:i]:
        d.update({s[i]:t[i]})
        k=k+1
    else:
        if d[s[i]]==t[i]:
            k=k+1
        else:
            k=k-1

if k==len(s):
    print(True)
else:
    print(False)

# if len(d)==len(s):
#     for j in range(0,len(s)):
#         if d[s[j]]==t[j]:
#             k=k+1
#         else:
#             print(False)
#             break
#     else:
#         print(True)
# else:
#     for j in range(0,len(l)):
#         if d[l[j]]==x[j]:
#             k=k+1
#         else:
#             print(False)
#             break
#     else:
#         print(True)









