#!/usr/bin/python3
"""
 using this REST API, for a given employee ID,
 returns information about his/her TODO list progress.
"""
from sys import argv
from requests import get


if __name__ == '__main__':
    try:
        id = int(argv[1])
    except IndexError and ValueError:
        print(f'usage: {argv[0]} <id>')
        quit(1)

    url = 'https://jsonplaceholder.typicode.com'
    user = get(f'{url}/users/{id}').json()
    todos = get(f'{url}/todos', params={'userId': id}).json()
    completed_todos = list(
        filter(
            lambda todo: todo['completed'] is True,
            todos
        )
    )

    if user == {}:
        print(f'no user with id {id}')
        quit(1)

    print(
        f"Employee {user['name']} is done with "
        f"tasks({len(completed_todos)}/{len(todos)}):"
    )

    for todo in completed_todos:
        print(f"\t {todo['title']}")
