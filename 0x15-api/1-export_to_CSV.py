#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""

import requests
import sys

if __name__ == "__main__":
    filename = "USER_ID.csv"
    user_id = sys.argv[1]
    user = requests.get(f"https://jsonplaceholder.typicode.com/user?{user_id}").json()
    todos = requests.get(f"https://jsonplaceholder.typicode.com/todos?{user_id}").json()

    completed = [t for t in todos]

    with open(filename, "w", encoding="utf-8") as file:
        for task in completed:
            file.write(
                task.get("id"),
                task.get("name"),
                task.get("completed"),
                task.get("title"),
            )

    # print(
    #     "Employee {} is done with tasks({}/{}):".format(
    #         user.get("name"), len(completed), len(todos)
    #     )
    # )

    # [print("\t {}".format(c)) for c in completed]
