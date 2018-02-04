f=open('input.txt')
st=f.readline().strip()
f.close()

result=''
past=st[0]
k=0
j=0
for i in st:
    if 'a'<=i<='z' or 'A'<=i<='Z':
        while k>0:
            result+=past
            k+=-1
        past=i
    else:
        k=10*k+int(st[j])
    j=j+1
while k > 0:
    result += past
    k += -1

f2=open("output.txt",'w')
f2.write(result)
f2.close()