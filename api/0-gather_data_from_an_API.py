#!/usr/bin/python3
"""
write a Python script that, using the given REST API,
for a given employee ID,
returns information about his/her TODO list progress
"""
import requests


def display_employee_progress(employee_id):
    """ script must display to stdout the employee TODO list progress """
    url = "https://jsonplaceholder.typicode.com"
    empl_url = f"{url}/users/{employee_id}"
    todo_url = f"{url}/todos"

    empl_response = requests.get(empl_url)
    empl_data = empl_response.json()
    todo_response = requests.get(todo_url,
                                 params={"userId": employee_id})
    todo_data = todo_response.json()

    empl_name = empl_data["name"]
    completed_tasks = [t["title"] for t in todo_data if t["completed"]]
    num_done = len(completed_tasks)
    num_total = len(todo_data)

    print("Employee {} is done with tasks({}/{}):"
          .format(empl_name, num_done, num_total))
    for t in completed_tasks:
        print("\t", t)

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("I don't think this thing should end up mattering")
        sys.exit(1)
    else:
        employee_id = int(sys.argv[1])
        try:
            display_employee_progress(employee_id)
        except requests.exceptions.RequestException:
            print("Well.. that didn't work \
                  (as far as I'm aware, this shouldn't print for checker)")
