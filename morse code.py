dict={"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--.."}
words = ["gin", "zen", "gig", "msg"]
t=""
l=[]
k=[]
for i in range(0,len(words)):
    for j in words[i]:
        t=t+dict[j]
    l.append(t)
    t=""
print(l)

for i in l:
    if i not in k:
        k.append(i)
print(len(k))