#!/usr/bin/python3
"""
write a Python script that, using the given REST API,
for a given employee ID,
returns information about his/her TODO list progress
"""
import urllib


def gather(id):
    """ script must display on stdout, the employee TODO list progress """
    empl = urllib.request("Employee", id)
    print(f"Employee {empl.name} is done with tasks({empl.tasks_done}/{empl.tasks}):\n")
    for t in empl.tasks_done:
        print(f"\t {t.title}\n")
