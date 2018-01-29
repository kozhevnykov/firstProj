import requests

api_link = "http://numbersapi.com/11/math?json=true"

f1 = open("input.txt",'r')
f2 = open("output.txt",'w')

for line in f1:
    api_link = "http://numbersapi.com/" + line.strip() + "/math?json=true"
    res = requests.get(api_link)
    data = res.json()
    if not data['found']:
        f2.write("Boring\n")
    else:
        f2.write("Interesting\n")

f1.close()
f2.close()