import requests
import json

arts = [line.strip() for line in open('input.txt')]

client_id = 'f37189045e6993c49822'
client_secret = 'e7052f903606ac36cf806672d5841feb'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]

# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token" : token}

dict = {}
"""for line in arts:
    r = requests.get("https://api.artsy.net/api/artists/"+line, headers=headers)
    j = json.loads(r.text)
    dict[j['birthday']] = j['sortable_name']
print(dict)
p = sorted(dict)
for i in range(len(p)):
    print(dict[p[i]])"""

