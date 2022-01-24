s="paper"
t="title"
if len(s)!=len(t):
    print(False)

dict1={}
dict2={}

for i in range(len(s)):
    s_ch=s[i]
    t_ch=t[i]
    if s_ch not in dict1:
        dict1[s_ch]=t_ch
    if t_ch not in dict2:
        dict2[t_ch]=s_ch
    if dict1[s_ch]!=t_ch or dict2[t_ch]!=s_ch:
        print(False)
print(True)



