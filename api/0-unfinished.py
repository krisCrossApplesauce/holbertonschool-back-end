#!/usr/bin/python3
""" returns information about to-do list progress """
import requests
import sys


def gather_api_data():
    """ gather and print api data """
    if(len(sys.argv) != 2):
        print("Error: not 3 arguments")

    employee_id = sys.argv[1]

    user_data = requests.get('https://jsonplaceholder.typicode.com/users/')
