import json
import requests

requests=requests.get('https://jsonplaceholder.typicode.com/users')
users = json.loads(requests.text)
print(users)

for user in users:
    print(f"Nome: {user['name']} Email: {user['email']}")
    