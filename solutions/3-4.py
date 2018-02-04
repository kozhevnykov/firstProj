n=int(input())
x=0
y=0
for i in range(n):
    st=input().split()
    if st[0]=='север':
        y=y+int(st[1])
    if st[0] == 'запад':
        x = x - int(st[1])
    if st[0]=='юг':
        y=y-int(st[1])
    if st[0]=='восток':
        x=x+int(st[1])

print(x,y)