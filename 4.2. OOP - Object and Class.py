

class Cat:
    '''
    ini adalah class untuk membuat object kucing
    melalui kelas ini kita bisa mendefinisikan nama dan tipe dari kucing yang dibuat

    PERATURAN:
    ketika membuat suatu methid dalam suatu kelas, 
    parameternya harus memuat 'self'
    sebagai keterangan bahwa method dan atribut adalah milik kelas CAT
    '''

    spesies = "kucing"

    def __init__(self, nama, tipe):         # adalah constractor, ketika fungsi dipanggiil makal fungsi ini akan langsung berjalan
        self.nama = nama
        self.tipe = tipe

    def run(self, speed):       # method, baru akan berjalan jika fungsi dipanggil
        print(f'kucing {self.nama} berlari dengan {speed}')

    def play(self):
        print(f'kucing {self.nama} bermain dengan kucing lainnya....')

    def eat(self):              #methode dalam kelas bisa lebih dari 1
        pass

# MEMBUAT OBJECT
Toha = Cat(nama = 'toha', tipe= 'anggora' )                # bem, 1 object sudah jadi
Kinako = Cat(nama='Kinako', tipe='anggora')
Minto = Cat(nama='Minto', tipe='anggora')

print(Toha)
print(Kinako)

print(Toha.tipe)

Kinako.run('cepat')             #mengakses metode kelas
Toha.play()                     #mengakses metode/fungsi kelas

print(Toha.__doc__)             # mengakses komen yang dibuat di kelas

print(f'Toha adalah kusing spesies {Toha.__class__.spesies}')           # mengakses variabel, tipe, nama, dll
print(f'Kinako merupakan kucing jenis {Kinako.tipe}')
print(f'{Minto.nama} merupakan kucing jenis {Minto.tipe}')

# Menghapus
del Kinako.tipe

print(Kinako)

print('=========================================================================') 

# Cintoh studi kasus data karyawan

class Employee():
    """
    ini adalah kelas untuk memenipulasi data karyawan
    melalui kelas ini kita dapat membaca, menghapus, dan menambah data 

    """
    def __init__(self, lokasi_file):
        self.data_employee = open(f'{lokasi_file}', mode = 'r', encoding = 'utf-8')
        self.data_per_sesi = 10

    def baca_data(self):
        self.data_employee = self.data_employee[:self.data_per_sesi]
        return self.data_employee

    def menghapus_data(self):
        del self.data_employee[baris][kolom]

    def menambah_data(self, data_baru):
        nama, gaji, jabatan = data_baru
        self.data_employee.append([nama, gaji, jabatan])

    def mengirim_data(self):
        pass

# Membuat Object
it = Employee(lokasi_file = './karyawan_it.xlx')
marketing = Employee(lokasi_file = './karyawan_marketing.xlx')

print('=========================================================================') 

# Object dalam AI
class Randomforest:
    pass