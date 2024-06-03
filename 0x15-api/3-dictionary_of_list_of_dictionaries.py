#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""

import json
import requests
import sys

if __name__ == "__main__":

    filename = "todo_all_employees.json"
    user_url = f"https://jsonplaceholder.typicode.com/users"
    todo_url = f"https://jsonplaceholder.typicode.com/todos"

    users = requests.get(user_url).json()
    todos = requests.get(todo_url).json()

    data = {}

    for user in users:
        user_id = user.get("id")
        data[user_id] = [
            {
                "username": user.get("username"),
                "task": todo.get("title"),
                "completed": todo.get("completed"),
            }
            for todo in todos
            if todo.get("userId") == user.get("id")
        ]

    with open(filename, "w", encoding="utf-8") as jsonfile:
        json.dump(data, jsonfile)
