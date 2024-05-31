#!/usr/bin/python3

"""Python script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress"""

import json
import requests
import sys


user_id = int(sys.argv[1])
user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"

# Getting the username
user_response = requests.get(user_url)
if user_response.status_code == 200:
    users = user_response.json()
    user_name = users["name"]

# Getting the todos
todo_reponse = requests.get(url)
if todo_reponse.status_code == 200:
    todos = todo_reponse.json()
    completed_task = [todo for todo in todos if todo["completed"]]


print(f"Employee {user_name} is done with tasks({len(completed_task)}/{len(todos)}):")
for tasks in completed_task:
    print(f"\t{tasks['title']}")
