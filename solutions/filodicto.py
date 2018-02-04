f1=open('input.txt','r')
st=f1.read().strip()
f1.close()

st=st.lower().split()
d={}

for i in st:
    if i in d.keys():
        d[i]=d[i]+1
    else:
        d[i]=1
st2=[]
ma = max( d.values() )
for key in d.keys():
    if d[key] == ma:
        st2.append(key)

st2.sort()

f2=open('output.txt','w')
f2.write(st2[0]+' '+str(ma))
f2.close()
