
def write_to_file(users):

    index = 1
    with open("users.txt","w") as f:
        for dct in users:
            f.write("User ID:"+ str(index) + "\n")
            f.write("Name:"+ dct['name'] + "\n")
            f.write("Age:"+ str(dct["age"]) + "\n")
            f.write("Address:"+ dct["address"] + "\n")
            f.write("Prefered_language:"+ dct["prefered_language"] + "\n")
            f.write("Gender:"+ dct["gender"] + "\n\n")
            index += 1


users = [{"name":"Aggy Cholomin","age":82,"address":"8961 Grim Street","prefered_language":"Dzongkha","gender":"Female"},
{"name":"Emmaline Bebis","age":57,"address":"3654 Boyd Center","prefered_language":"Norwegian","gender":"Female"},
{"name":"Shena Jeandot","age":19,"address":"36 Transport Parkway","prefered_language":"Dari","gender":"Female"},
{"name":"Zondra Strowan","age":25,"address":"0 Mayfield Parkway","prefered_language":"Belarusian","gender":"Female"},
{"name":"Claire Vasilyonok","age":31,"address":"6 Knutson Drive","prefered_language":"Hungarian","gender":"Female"},
{"name":"Genvieve Wadly","age":35,"address":"203 Clemons Park","prefered_language":"Malayalam","gender":"Female"},
{"name":"Winslow Crowley","age":46,"address":"57 Oneill Road","prefered_language":"Greek","gender":"Male"},
{"name":"Orsola Bellany","age":55,"address":"9219 Harper Park","prefered_language":"Hindi","gender":"Female"},
{"name":"Constantine Rugieri","age":84,"address":"8 Superior Road","prefered_language":"Tajik","gender":"Female"},
{"name":"Haleigh Poulney","age":69,"address":"07837 Shasta Place","prefered_language":"Zulu","gender":"Male"}]

write_to_file(users)

