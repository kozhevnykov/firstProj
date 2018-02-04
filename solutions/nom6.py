
f1=open('input.txt')
f2=open('output.txt','w')

n=f1.read().split()

if int(n[0])>=int(n[1])+int(n[2]):
    f2.write('YES')
else:
    f2.write('NO')
f1.close()
f2.close()