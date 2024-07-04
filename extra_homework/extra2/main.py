"""
users file ga yozilgan ma’lumotlarni qaytadan dict lardan tashkil topgan list ga
 joylashtiruvchi read_users_from_file(filename:str) → dict function ni bajaring.
   Ma’lumotlar dictinoriyga key va value file ga mos holatdan joylashishi kerak.  
"""

#code

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

print(read_users_from_file("users.txt")[0])