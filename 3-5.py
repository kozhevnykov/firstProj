import simplecrypt

with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()

f = open('passwords.txt','r')
for line in f:
    try:
        print(simplecrypt.decrypt(line.strip(),encrypted))
    except simplecrypt.DecryptionException:
        print('Not '+line.strip())
    else:
        print('Yes '+line)

