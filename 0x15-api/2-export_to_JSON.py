#!/usr/bin/python3

'''
Script for exporting employee data into json
'''

import json
import requests
from sys import argv


def get_employee_tasks(user_id):
    '''Retrieves employees and tasks'''
    root_url = 'https://jsonplaceholder.typicode.com/'
    user_req = root_url + 'users/{}'.format(user_id)
    employee = requests.get(user_req).json()
    employee_id = employee.get('id')
    task_req = root_url + 'todos?userId={}'.format(employee_id)
    tasks = requests.get(task_req).json()
    return {"employee": employee, "tasks": tasks}


def export_to_json(data):
    '''Exports dict to json'''
    _id = data.get('employee').get('id')
    _array = []
    for task in data.get('tasks'):
        new_dict = {}
        new_dict['task'] = task.get('title')
        new_dict['completed'] = task.get('completed')
        new_dict['username'] = data.get('employee').get('username')
        _array.append(new_dict)
    _dict = {
            _id: _array
         }
    with open('{}.json'.format(_id), 'w') as json_file:
        json.dump(_dict, json_file)


if __name__ == '__main__':
    data = get_employee_tasks(argv[1])
    export_to_json(data)
