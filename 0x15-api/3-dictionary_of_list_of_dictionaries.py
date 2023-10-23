#!/usr/bin/python3
"""
 using this REST API, for a given employee ID,
 returns information about his/her TODO list progress.
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
