#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""

import json
import requests
import sys

if __name__ == "__main__":

    user_id = sys.argv[1]
    filename = f"{user_id}.json"
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"

    user = requests.get(user_url).json()
    todos = requests.get(todo_url).json()

    with open(filename, "w", encoding="utf-8") as jsonfile:
        json.dump(
            {
                user_id: [
                    {
                        "task": t.get("title"),
                        "completed": t.get("completed"),
                        "username": user.get("username"),
                    }
                    for t in todos
                ]
            },
            jsonfile,
        )
