"""
S3:

product_material.txt bazasida sizda

id - produkt ID raqami
product - produkt kodi
material - ishlab chiqarilgan materiali
price - narxi
is_available - omborda bor yo'qligi
berilgan

1. Maqasadingiz shu ma'lumotlar orasidan narxi 500 va 1000 dollar
orasida bo'lgan va omborda mavjud bo'lgan produktlar ID raqami va ishlab 
chiqarilgan materialini chop etish bo'ladi.
"""

#code


#file joylashuvini o`zgartirishingiz kerak ekan
with open("product_material.txt", "r") as f: 
    while True:
        data = (f.readline()).replace('\n', '')
        if not data:
            exit(1)
       
        data = data.split(",")
        data[3] = float(data[3].replace("$",''))

        if 500 < data[3] > 1000 and data[-1] == "true":
            print(data)

