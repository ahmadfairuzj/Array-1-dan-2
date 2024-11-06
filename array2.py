# deklarasi matriks
matriks = []

# meminta input pengguna untuk mengisi matriks 3x3
print("masukan elemen untuk matriks 3x3")
for i in range(3):
    baris = []
    for j in range(3):
        nilai = int(input(f"masukan elemen baris {i+1}, kolom {j+1} : "))
        baris.append(nilai)
    matriks.append(baris)


#transpose matriks
transpose = []
for i in range(3):
    baris = []
    for j in range(3):
        baris.append(matriks[j][i])
    transpose.append(baris)            

#menampilkan hasil transpose
print("\nhasil tranpose matriks: ") 
for baris in transpose:
    print(baris)  

