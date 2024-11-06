angka = []

# meminta input pengguna
for i in range(5):
    element = int(input(f"masukan angka ke-{i+1}:"))
    angka.append(element)

#mengurutkan angka dalam array
angka.sort()

#menampilkan array yg sudah diurutkan
print(f"array yg sudah diurutkan {angka}")