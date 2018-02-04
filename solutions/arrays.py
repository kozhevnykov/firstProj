a=[int(i) for i in input().split()]
a.sort()
i=0
while i < len(a) - 1:
    if a[i] == a[i+1]:
        print( a[i], end=' ')
        while a[i]==a[i+1]:
            i=i+1
            if i == len(a)-1:
                break
    i=i+1
