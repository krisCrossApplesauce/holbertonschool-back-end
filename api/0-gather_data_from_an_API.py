#!/usr/bin/python3
"""
write a Python script that, using the given REST API,
for a given employee ID,
returns information about his/her TODO list progress
"""
import requests
import sys

def gather(empl_id):
    """ script must display to stdout (print), the employee TODO list progress """
    url = "https://jsonplaceholder.typicode.com/users"
    empl_url = f"{url}/{empl_id}"
    todo_url = f"{empl_url}/todos"

    empl_response = requests.get(empl_url)
    todo_response = requests.get(todo_url)
    empl_data = empl_response.json()
    todo_data = todo_response.json()

    name = empl_data.get('name')
    num_done = sum(1 for t in todo_data if t['completed'] is True)

    print(f"Employee {name} is done with tasks({len(todo_data)}/{num_done}):\n")
    for t in todo_data:
        if t['completed'] is True:
            print(f"\t {t['title']}")

if __name__ == "__main__":
    gather(sys.argv[1])
