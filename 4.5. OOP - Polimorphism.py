
class Cat:
    def __init__(self):
        self.nama = 'Meong'
        self.tipe = 'Anggora'

    def forward(self):
        print(f'kucing berlari......')


class Bird:
    def __init__(self):
        self.nama = 'Erago'
        self.tipe = "Elang"

    def forward(self):
        print('Elang itu terbang')
        
def melaju(object):                             # ini adalah fungsi umum untuk mendukung konsep POLIMORPHISM
    object.forward()

kinako = Cat(); erago = Bird()

melaju(kinako)
melaju(erago)