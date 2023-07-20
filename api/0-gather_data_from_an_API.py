#!/usr/bin/python3
"""
write a Python script that, using the given REST API,
for a given employee ID,
returns information about his/her TODO list progress
"""
import requests


def display_employee_progress(employee_id):
    """ script must display to stdout the employee TODO list progress """
    url = "https://jsonplaceholder.typicode.com/users"
    empl_url = f"{url}/{employee_id}"
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

    print(f"Employee {empl_name} is done with \
          tasks({num_done}/{num_total}):")
    for t in completed_tasks:
        print(f"\t{t}")

if __name__ == "__main__":
    import sys

    if len(sys.argv) == 2:
        try:
            display_employee_progress(int(sys.argv[1]))
        except requests.exceptions.RequestException:
            print("Well.. that didn't work \
                  (as far as I'm aware, this shouldn't ever print)")
