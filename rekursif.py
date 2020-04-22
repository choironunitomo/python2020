def cetak_bilangan(angka):
    if angka>=0:
        return str(angka) + "," + (cetak_bilangan(angka-1))
    return ""



print(cetak_bilangan(9))