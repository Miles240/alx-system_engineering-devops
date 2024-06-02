#!/usr/bin/python3

"""Python script that, using this REST API, for a given employee ID,
returns information about his/her TODOS list progress"""

import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"

    # Getting the username
    user_response = requests.get(user_url)
    if user_response.status_code == 200:
        users = user_response.json()
        user_name = users.get("name")

    # Getting the todos
    todo_reponse = requests.get(url)
    if todo_reponse.status_code == 200:
        todos = todo_reponse.json()
        completed_task = [
            todo for todo in todos if todo.get("completed") is True
            ]

    print(
        f"Employee \
            {user_name} is done with tasks\
                ({len(completed_task)}/{len(todos)}):"
    )
    for tasks in completed_task:
        print(f"\t{tasks.get('title')}")
