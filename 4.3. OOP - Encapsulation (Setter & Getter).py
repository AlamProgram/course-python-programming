
class Mobil:
    def __init__(self, plat):
        self.plat = plat
        self.tipe = 'Avanza'
        self.kecepatan = 200 # km/jam
        self.__bensin = 40 # liter

    #getter
    def LihatMaksimumBensin(self):
        print(f'Maksimum bensin adalah {self.__bensin} liter')
    
    def LihatMaksimalKecepatan(self):
        print(f'kecepatan maksimal mobil avanza adalah {200} km / jam')

    #setter
    def AturMaksimalBensin(self, bensin):
        self.__bensin = bensin
        

# Membuat object

avanza = Mobil(plat = 'B 2453 XY')

print(avanza.plat)
print(avanza.tipe)

print("=========================================================================")

avanza.kecepatan = 100
print(avanza.kecepatan)

avanza.__bensin = 20
print(avanza.__bensin)            # mengacu ke variabel avanza.__bensin, hasilnya menjadi 20 (berubah dari nilai awal)

print("=========================================================================")


avanza.LihatMaksimumBensin()    # nilai maksimum bensin  tetap
avanza.AturMaksimalBensin(30)
avanza.LihatMaksimumBensin()     # nilai sudah berubah ke 30


