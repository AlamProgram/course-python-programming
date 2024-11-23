#  3.1 Python Advanced - List, Tuple, Dictionary
list1= ['apple', 'watermelon', 'banana']     # apple, dkk adalah element
print(list1)

list2= [2, 1, 2, 7, 4, 10]
list3 = [True, False, False]
list4 = ["abc", 34, True, 40]

list5 = [list1, list2, list3, list4]
print(list5)

print('===============================')

print(list1+list2)
# print(list1-list2)
print(list2+list2)

print('===============================')

list1.sort()
print(list1)

list1.reverse()
print(list1)

print('===============================')
list6 = list1.copy()
print(list6)

print('===============================')
# untuk mengethui berapa jumlah angka 3 di dalm list, hasilnya 0
print(list3.count(3))
print(list3.count(7))

print('===============================')
#

print('=============INDEXING==================')
#
fruit_list = ['apple', 'banana', 'watermolon', 'orange', 'mango']
print(fruit_list[1])
print('===============================')
print(fruit_list[0:3])
print('===============================')
print(fruit_list[0:3]) # yg ke 3 hany sebagai batas
print('===============================')
print(fruit_list[-2])# ke 2 terakhir
print('===============================')
print(fruit_list[-2:-1])# ke 2 terakhir
print('===============================')
fruit_list[1] = "avocado"
print(fruit_list)
print('============ Membership Test ===================')
print('avocado' in fruit_list)
print('avocado' not in fruit_list)

print('============ Menambahkan ===================')
fruit_list.append('kiwi')
print(fruit_list)

print('insert')
fruit_list.insert(1, 'jackfruit') # perlu menentukan di ana tempat / indeks tempat dia disisipkan
print(fruit_list)

print('exted')
fruit_list1 = ['egg fruit', 'star fruit', 'papaya']
fruit_list2 = ['durian', 'rambutan']
fruit_list1.extend(fruit_list2)
print(fruit_list1)

#print('============ Menghapus ===================)
# .remove()
fruit_list1.remove('durian')
print(fruit_list1)

# .pop()
fruit_list1.pop(2)
print(fruit_list1)

# del
del fruit_list1[1]
print(fruit_list1)

# .clear
fruit_list1.clear() # menghaus semua elemen
print(fruit_list1)

# del, menghapus data list, SEMUANYA
del fruit_list1
print(fruit_list1)

# Tuple
tuple1= ('apple', 'watermelon', 'banana')     # apple, dkk adalah element
print(tuple1)

tuple2= (2, 1, 2, 7, 4, 10)
tuple3= (True, False, False)
tuple4= ("abc", 34, True, 40)

fruit_tuple1 = ('apple', 'watermelon', 'banana', 'watermelon')
print(fruit_tuple1[1])
print(fruit_tuple1[1:3])
print(fruit_tuple1[-2:])

for fruit in fruit_tuple1:     #  semua elemen yang ada di dalam tuple akan dianggap sebagai variabel fruit, karena di for looop idak perlu mendeklarasikan variabel terlebih dahulu
  print(fruit)

# tupple tidak bisa di del, remove, insert, cleatr,
# tuple bisa lebih cepat diproses komputer, sehingga bisa dipake untuk meningkatkan performa koding


print('============ #print ==================')

# Dictionary

fruit_dic = {
    'nama' :'pisang',
    'jenis' : 'ambon',
    'harga' : 10000,
    'kode' : 241
}

print(fruit_dic)
print(fruit_dic['nama'])
fruit_dic['nama'] = 'mangga'
print(fruit_dic)

print('================= For Loop Dictionary ================')

for key, value in fruit_dic.items():
  print(key, value)

# atau bisa jua
for key in fruit_dic.keys():      # .keys() berfugsi untuk mendapatkan daftar semua kunci yang ada di dalam dictionary
  print(key, fruit_dic[key])      #  fruit_dic[key] berfungsi mendapatkan nilai dari keytertentu


print('================= Menghapus ================')
del fruit_dic['kode']
print(fruit_dic)

print('================= Dictionary di dalam Tuple atau list ================')

fruit_list_dic = [
    {'nama' :'pisang',
    'jenis' : 'ambon',
    'harga' : 10000,
    'kode' : 241},
    {'nama' :'salak',
    'jenis' : 'ambon',
    'harga' : 10000,
    'kode' : 241}

]

print(fruit_list_dic)


fruit_tuple_dic = (
    {'nama' :'pisang',
    'jenis' : 'ambon',
    'harga' : 10000,
    'kode' : 241},
    {'nama' :'salak',
    'jenis' : 'ambon',
    'harga' : 10000,
    'kode' : 241}
)

# Set

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Union
print(A.union(B))

# Intersection
print(A.intersection(B))
print(A & B)

# Difference,             hanya yang ada di A naun tidak ada di B
print(A.difference(B))
print(A - B)

# Syetric Differenc
print(A^B)