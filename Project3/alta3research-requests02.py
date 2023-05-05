"""

Goal:
Send a GET request to your flask API; it should target the endpoint that returns JSON
Take the returned JSON and 'normalize' it into a format that is easy for users to understand

author: joshuaerichardson
date: 2023-05-04

"""
import json
import requests

URL = "http://127.0.0.1:5000/all_tasks"

response = requests.get(URL)
print(response)

# Change from json to python dictionary
response = response.json()

print('The following is a list of all tasks for all users:')
for task in response:
    print(f'''
    User: {task['username']}
    Tasks: {task['task']})
    ''')
