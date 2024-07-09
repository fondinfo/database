#!/usr/bin/env python3
"""
@author  Alberto Ferrari - https://albertoferrari.github.io/
@license This software is free - https://opensource.org/license/mit
"""
import requests

name = input("Teacher name: ")

url = f"http://localhost:8000/?name={name}"

# Send the GET request to the server
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    print("Data from server::")
    print(response.text)
else:
    print(f"Error. Status code: {response.status_code}")
