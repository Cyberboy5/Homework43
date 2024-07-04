"""
3. Tasavvur qiling foydalanuvchi boshqa shahardan uchib kelmoq Lekin u shunday bir qiziq shartni aytadi:
- Men US davlatiga uchishim kerak. Meni har kuni soat 21:00da Zoomda meetingim bo'ladi.
 Shunga menga shunday reys tanlab beringki, qo'nish vaqti meetingdan kamida 1 soat oldin bo'lsin.
   Menga shu reyslarning barchasini ko'rsatsangiz, uchish vaqti qiziq emas.
"""

#code

with open("booking_data.txt", "r") as f: 

    counrty = input("\nEnter The Country:")
    print("\n%30s\n"%("Available Flights:"))

    while True:
        data = f.readline()
        if not data:
            break

        data = data.split(',')
      
        orginal_time1 = data[2]
        orginal_time2 = data[4]
    
        data[2] = data[2].split(":")
        data[4] = data[4].split(":")

        if (int(data[4][0]) < 20 and counrty == data[3]):
            data[2] = orginal_time1
            data[4] = orginal_time2
            is_here = True

            print(data)
        
if  not is_here:
    print("        No Valid Flights Found     ")

print()