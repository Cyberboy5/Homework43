"""
S5:
Foydalanuvchi son kiritadi vazifangiz quyidagi shaklda faylga ma'lumot yozish, agar son toq bo`lsa:
Input: 5
Output:
1=1
2+2=4
3+3+3=9
4+4+4+4=16
5+5+5+5+5=25
Agar son juft bo`lsa:
Input: 4
4+4+4+4=16
3+3+3=9
2+2=4
1=1
"""

#code

def write_to_file(n):
    with open("numbers.txt", "w") as f:
        if n % 2 == 0: 
            for i in range(n, 0, -1):
                line = '+'.join([str(i)] * i) + f"={i * i}\n"
                f.write(line)
        else:  
            for i in range(1, n + 1):
                line = '+'.join([str(i)] * i) + f"={i * i}\n"
                f.write(line)

#MAIN
number = int(input("Enter a number: "))
write_to_file(number)
