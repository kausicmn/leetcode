widths =[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
s = "abcdefghijklmnopqrstuvwxyz"
dict={"a":widths[0],"b":widths[1],"c":widths[2],"d":widths[3],"e":widths[4],"f":widths[5],"g":widths[6],"h":widths[7],"i":widths[8],
      "j":widths[9],"k":widths[10],"l":widths[11],"m":widths[12],"n":widths[13],"o":widths[14],"p":widths[15],"q":widths[16],
      "r":widths[17],"s":widths[18],"t":widths[19],"u":widths[20],"v":widths[21],"w":widths[22],"x":widths[23],"y":widths[24],
      "z":widths[25]}
t=0
z=""
u=0
for i in range(0,len(s)):
    t=t+dict[s[i]]
    if 0<=t<=100:
        z=z+s[i]
    if t>100:
        print(len(z))
        z=""
        z=z+s[i]
        t=0
        t=t+dict[s[i]]
        u=u+1
print([u+1,t])


