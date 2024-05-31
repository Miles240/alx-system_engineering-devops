import requests
import json


response = requests.get("https://freetestapi.com/api/v1/users?limit=5")

datas = response.json()

print(datas)
# for data in datas:
# 	print(data)
