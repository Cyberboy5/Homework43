"""
Filedan olingan ma’lumotlarni users.json file ga chiroyli tartibda yozing.
JSON file:
[
    {
        "id": 1,
        "name": "Aggy Cholomin",
        "age": 82,
        "address": "8961 Grim Street",
        "prefered_language": "Dzongkha",
        "gender": "Female"
    },
...
...
...
    {
        "id": 10,
        "name": "Haleigh Poulney",
        "age": 69,
        "address": "07837 Shasta Place",
        "prefered_language": "Zulu",
        "gender": "Male"
    }
]

"""

# code

import json

def read_users_from_file(filename:str)-> dict:

    with open(filename, 'r') as f:
        data = f.read()

    users = []

    blocks = data.split("\n\n")
    for i ,block in enumerate(blocks):
        blocks[i] = block.split("\n")
        blocks[i].pop()
        user = {}
        for field in blocks[i]:
            pair = field.split(":")
            user[pair[0]] = pair[1]
        users.append(user)
    return users

users = read_users_from_file('users.txt')

with open("users.json","w") as f2:
    json.dump(users, f2,indent=4)
