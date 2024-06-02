#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""

import csv
import requests
import sys

if __name__ == "__main__":

    user_id = sys.argv[1]
    filename = f"{user_id}.csv"
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"

    user = requests.get(user_url).json()
    todos = requests.get(todo_url).json()

    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow(
                [
                    user_id,
                    user.get("username"),
                    task.get("completed"),
                    task.get("title"),
                ]
            )
