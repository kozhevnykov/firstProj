n=int(input())
a=[]
for i in range(n):
    a.append([])
    for j in range(n):
        a[i].append(0)
for i in range(n):
    a[0][i]=i+1

    
for i in range(n):
    for j in range(n):
        print(a[i][j],end=' ')
    print()