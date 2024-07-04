"""
S4:

booking_data.txt faylida quyidagi ma'lumotlar keltirilgan

id - ID raqami
departure - uchib ketish davlati
d_time - uchish vaqti
arrive - qo'nish davlati
a_time - qo'nish vaqti
cost - bilet narxi

1. Foydalanuvchi o'zida bor taxminiy pul miqdorini kiritadi. 
Maqsadingiz shu kiritlgan summadan $50 arzonroq va 
$100 qimmatroq bo'lgan biletlar ro'yhatini ko'rsatish
"""

#code

with open("booking_data.txt", "r") as f: 

    data = (f.read()).replace('$','')
    data = data.split('\n')[:-1]

budjet = float(input("Enter Your Budget:"))
print("\n%30s\n"%("Books:"))

for i ,val in enumerate(data):
    data[i] = val.split(',')    
    if float(data[i][-1])-50 < budjet or float(data[i][-1])+100 > budjet:
        print(data[i])

