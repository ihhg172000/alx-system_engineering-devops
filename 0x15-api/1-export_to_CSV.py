#!/usr/bin/python3
"""
 using this REST API, for a given employee ID,
 returns information about his/her TODO list progress.
"""
import csv
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

    with open(f'{id}.csv', 'w') as file:
        writer = csv.writer(
            file,
            delimiter=',',
            quotechar='"',
            quoting=csv.QUOTE_ALL
        )

        for todo in todos:
            writer.writerow(
                [
                    user['id'],
                    user['username'],
                    todo['completed'],
                    todo['title']
                ]
            )
