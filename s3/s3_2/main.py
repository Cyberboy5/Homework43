"""
2. Foydalanuvchi material nomini kiritadi va siz unga barcha omborda hozirda mavjud 
(true) bo'lgan produktlar narxlarini o'sish tartibida chiqarib berishingiz lozim
"""

#code

with open("product_material.txt", "r") as f: 
 
    prices = []
    material = input("\nMaterial:")
    print("\n%30s\n"%("Products:"))
   
    while True:
      
        data = (f.readline()).replace('\n', '')  
        if not data:

            prices.sort()
            print(f"\n        Prices:\n\n{prices}")
            print()

            exit(1)
       
        data = data.split(",")
        data[3] = float(data[3].replace("$",''))

        if material == data[2] and data[-1] == "true":
            prices.append(data[3])
            print(data)
