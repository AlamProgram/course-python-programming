

# While Loop
count = 0

while count < 9:
    print("nilai count adalah ", count)
    count = count + 1

print("stop while loop.")

list_angka = [1,2,3,4,5,6,7,8,9]                    #  bisa pake LIST, DICTIONARY, TUPPLE

for x in list_angka:
    print(x)

print("for loop stop.")

list_range = list(range(10))                         # Penulisan angka juga bisa dipersingkat dgn range 
print(list_range)                                   #akan print 0 - 9 

#bisa juga kaya gini
list_range_2 = list(range(2,7))
print(list_range_2)

#================================================================

i =90

while (i < 100):
    j = 2
    print(i/j)
    while ( j <= (i/j) ):
        print('loop dalam loop')
        j= j +1
        i = i + 1
print("selamat tinggal")

print("============ Break ===================")

for var in "string":
    

    if var == "i":
        break                   #ketika sampai di 'i" maka akan lanjut ke perintah selanjutnya

    print(var)

print("selamat tinggal")

print("============ Continue ===================")

for val in "selamat jalan":

    if val == "j":
        continue                                        #jika sampai pada j, perintah selanjutnya akan diskip dan akan lanjut loop

    print(val)

print("selamat tinggal")



print("============ For Else ===================") 

daftar_murid = ["angga", "mardadi", "rowi"]             # untuk mencari apakah suatu elemen ada di himpunan yang kita cari atau tidak
nama_murid= "farhan"

for nama in daftar_murid:

    if nama == nama_murid:
        print(nama)
        break

else:
    print("nama murid tidak ada")


print("============ pass ===================") 
                                                    # berguna kalau belum mau / belum tau aksi alternatif yg mau diisi apa
daftar_murid = ["angga", "mardadi", "rowi"]           

for nama in daftar_murid:

    if daftar_murid == 0:
        pass    

    else:
        pass




