#!/usr/bin/python3
"""
 using this REST API, for a given employee ID,
 exports information about his/her TODO list progress to json file.
"""
import json
from requests import get
from sys import argv


if __name__ == '__main__':
    try:
        id = int(argv[1])
    except IndexError and ValueError:
        print(f'usage: {argv[0]} <id>')
        quit(1)

    url = 'https://jsonplaceholder.typicode.com'
    user = get(f'{url}/users/{id}').json()
    todos = get(f'{url}/todos', params={'userId': id}).json()

    if user == {}:
        print(f'no user with id {id}')
        quit(1)

    with open(f'{id}.json', 'w') as file:
        json.dump(
            {
                user['id']: [
                    {
                        'task': todo['title'],
                        'completed': todo['completed'],
                        'username': user['username']
                    }
                    for todo in todos
                ]
            },
            file
        )
