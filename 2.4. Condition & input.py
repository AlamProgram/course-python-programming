

# CONDITION
jumlah_pemunpang = 10

if jumlah_pemunpang > 10:
    print("mobil jalan....")

if jumlah_pemunpang < 10:
    print("mobil diam...")

score = 78
if score  > 78:
    print("lulus")
elif score < 10:
    print("tidak lulus")

if score >=85:
    print("Peringkat A/ Memuaskan")

elif score >= 75:
    print("Peringkat B/Bagus")

else:                           # selain kondisi kedua diatas, maka jalankan perintah else
    print("Tidak Lulus")


#============================================================================================
kelas = 1
score = 90

if kelas >1:
    if score >=85:
        print("Peringkat A/ Memuaskan")
    elif score >= 75:
        print("Peringkat B/Bagus")
    else:                          
        print("Tidak Lulus")


else:
    if score >=80:
        print("Peringkat A/ Bagus")   
    else:                          
        print("Tidak Lulus")

#============================================================================================

num = float(input("masukan angka!...."))  # jika angka yang dimasukkan di terminal -2, maka tidak akan menjalankan apa2

if num == 0:
    print("angka 0")

else:
    print("angka positif")
