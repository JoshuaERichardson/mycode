'''

Goal:
Send a GET request to your flask API; it should target the endpoint that returns JSON
Take the returned JSON and 'normalize' it into a format that is easy for users to understand

author: joshuaerichardson
date: 2023-05-04

'''
from flask import Flask, request, jsonify
from pprint import pprint

URL = "http://127.0.0.1:2224"

def main():
    r = request.get(URL + "/api/v1/users")
    pprint(r.json())

if __name__ == "__main__":
    main()

