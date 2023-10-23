#!/usr/bin/python3
"""
 using this REST API,
 exports all tasks from all employees to json file.
"""
import json
from requests import get


if __name__ == '__main__':

    url = 'https://jsonplaceholder.typicode.com'
    users = get(f'{url}/users').json()

    todo_all_employees = {}

    for user in users:
        todos = get(f'{url}/todos', params={'userId': user['id']}).json()
        todo_all_employees[user['id']] = [
            {
                'username': user['username'],
                'task': todo['title'],
                'completed': todo['completed']
            }
            for todo in todos
        ]

    with open('todo_all_employees.json', 'w') as file:
        json.dump(todo_all_employees, file)
