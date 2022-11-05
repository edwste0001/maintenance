import sys

strname = "test\\za\\Untitled.png"
strname2 = "qqqqqqqqqqqqqqq\\test\\za\\Untitled.png"

f=open(strname,'rb')
f2=open(strname2,'rb')

#fout=open(strname + '.dump', 'w+')
#fout2=open(strname2 + '.dump', 'w+')

s = f.read()
s2 = f2.read()

for i,j in enumerate(zip(s,s2)):
    k,l = j
    if k!=l:
        print(hex(i),"\t",chr(k),":",k,":",hex(k),"\t",chr(l),":",l,":",hex(l),"difference found\t")


#print(s,file=fout)
#print(s2,file=fout2)

f.close()
f2.close()

#fout.close()
#fout2.close()
