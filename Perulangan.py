i = 1
while i <= 10:
    print(i)
    i += 1

print(("Akhir dari loop"))

rahasia ="Unitomo"
tebak = ""
batas = 3
while rahasia != tebak and batas>0:
    tebak = input("Tebak kata :")
    if tebak==rahasia:
        print("Yes, Anda benar!")
    else:
        batas -= 1
        if batas == 0:
            print("Sudah 3x salah.")
        else:
            print("Masih salah. Ayo tebak lagi.")