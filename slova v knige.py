def f(y):
    return y/2

n=int(input())
d={}
for i in range(n):
    x=int(input())
    if x in d.keys():
        print(d[x])
    else:
        d[x]=f(x)
        print(d[x])

