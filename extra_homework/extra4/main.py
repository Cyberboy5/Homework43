"""
users.json file dan ma’lumotlarni o’qing va name field ni o’rniga ynagi first_name va last_name field larni qo’shing va file ga qayta yozing.

New JSON file:
[
    {
        "id": 1,
        "first_name": "Aggy",
        "last_name" : "Cholomin",
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
        "Name": "Haleigh",
        "last_name" : "Poulney"
        "age": 69,
        "address": "07837 Shasta Place",
        "prefered_language": "Zulu",
        "gender": "Male"
    }
]

 Note:Last va First namelarni Nameni orniga ilib kelish ni yo`lini topa olmadim

"""

#code

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


# MAIN
users = read_users_from_file('users.txt')[:-1]

for i ,dct in enumerate(users):

    student = dct['Name'].split(' ')

    first_name, last_name = dct['Name'].split()
    dct['First_name'] = first_name
    dct['Last_name'] = last_name
    
    del dct['Name']


with open("users.json","w") as f2:
    json.dump(users, f2,indent=4)
