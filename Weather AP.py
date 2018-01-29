import requests

api_url = "http://api.openweathermap.org/data/2.5/weather"

city = input("GOROD? ")

params = {
    'q' : city,
    'appid' : 'f3dc189de9d9eaa2bb31d0a2db957fdf',
    'units' : 'metric'
}

res = requests.get(api_url, params = params)
#print(res.status_code)
#print(res.headers["Content-Type"])
#print(res.json())

data = res.json()
print(data["main"]["temp"])

