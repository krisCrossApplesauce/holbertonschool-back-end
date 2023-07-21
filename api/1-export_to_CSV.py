#!/usr/bin/python3
"""
using what didn't work in task 0 :D
extend your Python script to export data in the CSV format
"""
import csv
import requests


def export_empl_prog_to_csv(user_id):
    """ why """
    url = "https://jsonplaceholder.typicode.com"
    empl_url = f"{url}/users/{user_id}"
    todo_url = f"{url}/todos"

    empl_data = requests.get(empl_url).json()
    todo_data = requests.get(todo_url,
                             params={"userId": user_id}).json()

    empl_name = empl_data.get("name")
    user_name = empl_data.get("username")
    completed_tasks = [t["title"] for t in todo_data if t["completed"]]
    num_done = len(completed_tasks)
    num_total = len(todo_data)

    with open(f'{user_id}.csv', 'w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for todo in todo_data:
            writer.writerow((user_id, user_name,
                             todo["completed"], todo["title"]))

    print("Employee {} is done with tasks({}/{}):"
          .format(empl_name, num_done, num_total))
    for task in completed_tasks:
        print(f"\t {task}")


if __name__ == "__main__":
    import sys

    export_empl_prog_to_csv(int(sys.argv[1]))
