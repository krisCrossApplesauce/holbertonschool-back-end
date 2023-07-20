#!/usr/bin/python3
""" returns information about to-do list progress """
import requests
import sys


def display_employee_progress():
    """ gather and print api data """
    if(len(sys.argv) != 2):
        print("Error: not 3 arguments")

    employee_id = sys.argv[1]

    user_data = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                             .format(employee_id)).json()
    todo_data = requests.get('https://jsonplaceholder.typicode.com/todos',
                             params={"userId": employee_id}).json()
    EMPLOYEE_NAME = user_data.get("name")
    completed_tasks = [todo.get("title") for todo in todo_data if todo["completed"]]
    NUMBER_OF_DONE_TASKS = len(completed_tasks)
    TOTAL_NUMBER_OF_TASKS = len(todo_data)

    print('Employee {} is done with tasks({}/{}):'
          .format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for task in completed_tasks:
        print("\t {}".format(task))


if __name__ == "__main__":
    display_employee_progress()
