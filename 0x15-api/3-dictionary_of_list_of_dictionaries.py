#!/usr/bin/python3
"""
Module 3-dictionary_of_list_of_dictionaries
Export this data to JSON
"""
import json
import requests


def all_to_json():
    """return API data"""
    USERS = []
    userss = requests.get("https://jsonplaceholder.typicode.com/users")
    for u in userss.json():
        USERS.append((u.get('id'), u.get('username')))
    TASK_STATUS_TITLE = []
    todos = requests.get("https://jsonplaceholder.typicode.com/todos")
    for t in todos.json():
        TASK_STATUS_TITLE.append((t.get('userId'),
                                  t.get('completed'),
                                  t.get('title')))

    """export to json"""
    data = dict()
    for u in USERS:
        t = []
        for task in TASK_STATUS_TITLE:
            if task[0] == u[0]:
                t.append({"task": task[2], "completed": task[1],
                          "username": u[1]})
        data[str(u[0])] = t
    filename = "todo_all_employees.json"
    with open(filename, "w") as file:
        json.dump(data, file, sort_keys=True)


if __name__ == "__main__":
    all_to_json()
