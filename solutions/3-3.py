n=int(input())
dic=[]
for i in range(n):
    dic.append(input().lower())

n=int(input())
for i in range(n):
    st=input().lower().split()
    for j in range(len(st)):
        if st[j] not in dic:
            print(st[j])
            dic.append(st[j])
