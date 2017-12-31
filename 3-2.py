l=input()
l1=[x for x in l]
l=input()
l2=[x for x in l]
l=input()
l3=[x for x in l]
l=input()
l4=[x for x in l]

for i in range(len(l3)):
    print(l2[l1.index(l3[i])],end='')
print()

for i in range(len(l4)):
    print(l1[l2.index(l4[i])], end='')
print()
