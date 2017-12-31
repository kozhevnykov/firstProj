def addvalue(val,res):

    if val not in d.keys():
        d[val]=[1,0,0,0]
        if res==0:
            d[val][1]=0
            d[val][2]=0
            d[val][3]=1
        elif res==1:
            d[val][1] = 0
            d[val][2] = 1
            d[val][3] = 0
        else:
            d[val][1] = 1
            d[val][2] = 0
            d[val][3] = 0
    else:
        d[val][0]+=1
        if res==0:
            d[val][3]+=1
        elif res==1:
            d[val][2]+=1
        else:
            d[val][1]+=1



n=int(input())
d={}

for i in range(n):
    st=input().split(';')
    if st[1]==st[3]:
        addvalue(st[0],1)
        addvalue(st[2],1)
    if st[1]>st[3]:
        addvalue(st[0],3)
        addvalue(st[2],0)
    if st[1]<st[3]:
        addvalue(st[0],0)
        addvalue(st[2],3)

for key in d.keys():
    print(str(key)+':',end='')
    print(d[key][0],d[key][1],d[key][2],d[key][3],end=' ')
    print(d[key][1]*3+d[key][2])
