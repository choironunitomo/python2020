angka1 = input("Masukkan Angka 1 =")
angka2 = input("Masukkan Angka 2 =")

if not (angka1>angka2):
    print(angka1, " Lebih dari ", angka2)
elif (angka1<angka2):
    print(angka1, " kurang dari ", angka2)
else:
    print(angka1, " sama dengan ", angka2)

Pria = True
Jomblo = False

if Pria and not Jomblo:
    print("Anda seorang pria pemberani")
else:
    print("Anda seorang pria payah")

def max_num(num1, num2, num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    else:
        return num3

print(max_num(30,20,32))
print(max_num(4,10,3))