#!/usr/bin/python3
""" return information about todo list"""

import sys
import requests as req

if __name__ == "__main__":
    api = 'https://jsonplaceholder.typicode.com/'
    idx = sys.argv[1]
    values = {'userId': idx}

    user = req.get(api + 'users/{}'.format(idx)).json()
    tasks = req.get(api + 'todos',params=values).json()

    finished = [ task.get('title') for task in tasks if task.get('completed') == True]

    print('Employee {} is done with tasks({}/{}):'.format(user.get('name'), len(finished), len(tasks)))

    for task in finished:
        print('\t {}'.format(task))
