

angka = 10
print(angka)

angka = 100
# yang diprint akan 10, karena phyton mengeksekusi secara sequencial 

angka1, angka2, email = 10, 0.5, "ya email"

print (angka1)
print(angka2)
print(email)

angka1 = angka2 = angka3 = 100
print(angka1)
print(angka2)
print(angka3)  # maka yang diprint nilainya 100 semua

#Konstanta
# variabel pake huruf kapital semua
GRAVITY = 9.8
PI = 22/7

# Literal
nomor_biner = 10110011
print(nomor_biner)

nomor_float = 2.34e10
print(nomor_float)

#--------------------------------------

a = 3
print(type(a))

b = 2.0
print(type(b))

c = 22.7
print(type(c))

d = a+c
print(type(d))

e = float (a)
print(type(e))

c= int(c)
print(type(c))
print (c)

a= str(a)
print(a)

c = 8/5
c= c.__ceil__()
print(c)

c = 8/5
c= c.__float__()
print(c)

c = "ini adalah string single line"
print(c)

c  = '''
ini adalah string
mutiline
'''
print(c)

s = "Ini adalah single line"
print(s)

s = s.lower()
print(s)

s = s.upper()
print(s)

s = s.replace('ADALAH', 'MERUPAKAN')
print(s)

nama= 'Alam'
s = f"nama saya adalah {nama}"
print (s)

#atau
#nama ="dzul"
#s= f"nama saya adalah {}".format(nama)
#print(s)


#----------------------------------------------------------
b= True
print(type(b))

# konsep logika
# true and true = true
# true and false = false
#

print(True and False)
# atau
print(True & False)

print(True or False)
# atau
print(True|False)

# List, Tuple, Dictionary
L = [1, 2.2, 'nama']
print(l)
print(type(l))

T = (1, 2,2, 'nama')
print(T)
print(type(T))

D = {'key1':'value1', 'key1':'value2'}
print(D)
print(type(D))