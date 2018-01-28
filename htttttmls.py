import requests
import re

a,b = input(), input()
t=0
first = requests.get(a.strip())
urls = re.findall(r"href=\"(https.+)\"",first.text)
for i in urls:
    second = requests.get(i.strip())
    url = re.findall(r"href=\"(https.+)\"", second.text)
    if b.strip() in url:
        print("Yes")
        t=1
        break
if t == 0:
    print("No")