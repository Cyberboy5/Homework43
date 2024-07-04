"""
2. Kiritilgan davlat bo'yicha barcha aviareyslarni toping.
Lekin chiqishda faqat soat 12:00dan 21:00gacha bo'lgan reyslar chiqsin.
"""

#code

is_here = False

with open("booking_data.txt", "r") as f: 

    counrty = input("\nEnter The Country:")
    print("\n%30s\n"%("Books:"))

    while True:
        data = f.readline()
        if not data:
            break

        data = data.replace('$', '').strip()
        data = data.split(',')
      
        orginal_time1 = data[2]
        orginal_time2 = data[4]
    
        data[2] = data[2].split(":")
        data[4] = data[4].split(":")

        if int(data[4][0]) > 12 and int(data[4][1]) < 21 and counrty == data[1]:
            data[2] = orginal_time1
            data[4] = orginal_time2
            is_here = True
            print(data)
        
if  not is_here:
    print("        No Valid Books Found")

print()

