def change_str(st):
    if st.find(a) != -1:
        return st[0:st.find(a)] + b + change_str(st[st.find(a)+len(a)::])
    else:
        return st

s = input()
a = input()
b = input()

if s.find(a) == -1:
    print(0)
elif b.find(a) != -1:
    print("Impossible")
else:
    t=0
    while True:
        if s.find(a) != -1:
            s = change_str(s)
            # print(s)
            t=t+1
        else:
           print(t)
           break
