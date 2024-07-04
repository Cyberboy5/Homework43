


with open("product_material.txt", "r") as f: 
  
    material = []
    print("\n%30s\n"%("Materials:"))
  
    while True:
        data = (f.readline()).replace('\n', '')
        if not data:
            print(f"\nMaterials: \n\n{material}\n")
            exit(1)
       
        data = data.split(",")
        data[3] = float(data[3].replace("$",''))

        if data[3] < 1000 and data[-1] == 'false':
            material.append(data[2])
            print(data)
