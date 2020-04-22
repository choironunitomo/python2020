print("Hello World")

char_name = "ACHMAD CHOIRON"
int_age = 45
bol_status= True
print("my name is "+ char_name)
print(" I am ", int_age, " years old")
print("I am a lecturer at Unitomo.",bol_status)
print("Cetak double quote \" dengan menambahkan karakter \\")

char_frase = "Universitas Dr. Soetomo"
print(char_frase + "adalah kampus kebangsaan dan kerakyatan")
print(char_frase.upper() + " " + char_frase.lower())
print(char_name.isupper())
print(char_name.islower())
print(char_name[3] * 10)
print(char_name[0:5])
print(char_name[0:5:3])
print(char_name.index('N'))

print(2+3*3.0)
print(10 % 3)
print(10 / 3)

my_number = 5
print(str(my_number) + " My fvourite number")

my_number = -5
print(abs(my_number))
print(pow(3,8))
print(round(3.255))

from math import *
print(sqrt(36))
print(floor(3.7))
print(ceil(3.2))