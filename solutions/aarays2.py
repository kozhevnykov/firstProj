a=input().split()
m=0
n=len(a)
s=[]
while a!=['end']:
    s.append([int(i) for i in a])
    m+=1
    a=input().split()

for j in range(m):
    for i in range(n):
            print(s[j][(i+(n>1))%n]+s[j][i-(n>1)]+s[(j+(m>1))%m][i]+s[j-(m>1)][i], end=' ')
    print()