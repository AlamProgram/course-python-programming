
#Parent Class
class Animal:

    def __init__(self):
        self.tipe = "Mamalia"
        self.kecepatan = 'lambat'

    def grow(self):
        print('mamalia ini bertumbuh')
    
#Child Class
class Cat(Animal):                          #harus ada   

    '''Syarat Shild Class, jarus ada:
    1. Parameter Nama Kelas Induk (Animal)
    2. super().__init__()        di fungsi konstraktor'''

    def __init__(self, nama, tipe):
        
        super().__init__()
        
        self.nama  = nama
        self.tipe = tipe

    def run(self):
        
        print(f'kicing {self.tipe} bisa berlari')

kinako = Cat(nama= 'Kinako', tipe = 'Anggora')

print(kinako.kecepatan)
print(kinako.tipe)                  # karena berlaku konsep 'Overriding' maka tipe parent diperbarui dengan tipe child

kinako.run()
kinako.grow()                       # tetap bisa mengakses fungsi dari Parent/Mamalia



