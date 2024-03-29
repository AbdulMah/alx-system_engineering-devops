#!/usr/bin/python3
"""
Module 0-gather_data_from_an_API
Using https://jsonplaceholder.typicode.com/
"""

from sys import argv
import csv
import requests


def gather_data_to_csv():
    """Fetches data of employees
        and their todo tasks
    """

    users_url = "https://jsonplaceholder.typicode.com/users"
    users = requests.get(users_url)
    for i in users.json():
        if i.get("id") == int(argv[1]):
            USERNAME = i.get("username")
            break
    TASK_STATUS_TITLE = []
    todos = requests.get("http://jsonplaceholder.typicode.com/todos")
    for t in todos.json():
        if t.get('userId') == int(argv[1]):
            TASK_STATUS_TITLE.append((t.get('completed'), t.get('title')))

    """export to csv"""
    filename = "{}.csv".format(argv[1])
    with open(filename, "w") as csvfile:
        fieldnames = ["USER_ID", "USERNAME",
                      "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,
                                quoting=csv.QUOTE_ALL)
        for task in TASK_STATUS_TITLE:
            writer.writerow({"USER_ID": argv[1], "USERNAME": USERNAME,
                             "TASK_COMPLETED_STATUS": task[0],
                             "TASK_TITLE": task[1]})


if __name__ == "__main__":
    gather_data_to_csv()
