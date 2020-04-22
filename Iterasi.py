for letter in "Universitas Dr. Soetomo" :
    print(letter)

for index in range(5,10):
    print(index)

friends = ["Joni","Ali","Sukma","Tejo","Kompas"]
print((len(friends)))
print(friends)
print(friends.index("Ali"))
print(friends[2])

for friend in friends:
    print(friend)
print("_" * 20)
for indeks in range(3,len(friends)):
    print(friends[indeks])

print("X" * 20)

def pangkat(a,b):
    if b>0 :
        return a * pangkat(a, b-1)
    else:
        return 1

print(pangkat(3,1))

print("X" * 20)

def fungsi_pangkat(a,b):
    hasil = 1
    for idx in range(b):
        hasil *= a
    return hasil

print(fungsi_pangkat(3,3))
