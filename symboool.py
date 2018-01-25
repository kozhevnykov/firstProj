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
        t += 1
        if s.find(a) != -1:
            s2 = s[0:s.find(a)] + b + s[s.find(a)+len(a)::]
            s = s2
            print(s)
        else:
           print(t)
           break
