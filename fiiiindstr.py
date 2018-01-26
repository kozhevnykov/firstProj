def fi(s):
    if t in s:
        return 1 + fi(s[s.find(t)+1::])
    else:
        return 0

s,t = [input() for i in range(2)]

print(fi(s))