f1=open('input.txt')
f2=open('output.txt','w')
d={}
st2=[0,0,0,0]
k=0
for line in f1:
    st=line.strip().split(';')
    d[st[0]]=[st[1:4]]
    f2.write(str((int(st[1])+int(st[2])+int(st[3]))/3)+'\n')
    st2[1] += int(st[1])
    st2[2] += int(st[2])
    st2[3] += int(st[3])
    k=k+1

f2.write(str(int(st2[1])/k)+' ')
f2.write(str(int(st2[2])/k)+' ')
f2.write(str(int(st2[3])/k))

f1.close()
f2.close()