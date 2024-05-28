#!/usr/bin/python3

"""Python script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress"""

import json
import requests
import sys

base_url = "https://jsonplaceholder.typicode.com"
user_id = sys.argv[1]
user_name = ""
user_url = f"{base_url}/users"

response = requests.get(user_url)

if response.status_code == 200:
	users = response.json()
	for user in users:
		if user['id'] == user_id:
			user_name = user['name']

print(user_name)


