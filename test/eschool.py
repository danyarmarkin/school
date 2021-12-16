import requests, json

url = 'https://app.eschool.center/ec-server/role/checkRegCode'

params = {"strCode": "CODE", "challenge": "true", "response": "true"}

r = requests.get(url, params)
print(r.url)