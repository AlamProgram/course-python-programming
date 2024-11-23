# File Handling
#Read
data = open ('./data.txt', mode = 'r')
print(data.read())

data = open ('./data.txt', mode = 'r', encoding = 'utf - 8') # direkomendasikan, karena biasanya kakau axa file yg tidakbbisa terbaca, biasanya karen dia memiliki encodongvyg berbeda atau bukan utf - 8
print(data.read())

string = data.read()
print (string)

print('================= Append / menambahkan =================')

data = open ('./data.txt', mode = 'a', encoding = 'utf - 8')
data.write('/n semangat belajar Python, biar ak stak di karir') # harusnya slash n, slsh n untuk menambahkan teks di line yang baru
data.write('/n harus banyak laihan biar jago')
data.close()  # untuk membebaskn memori yang dipakai


print('================= Write / menulis baru, yg lama dihapus ===========')

data = open ('./data.txt', mode = 'w', encoding = 'utf - 8')
data.write('/n semangat belajar Python, biar ak stak di karir') # harusnya slash n, slsh n untuk menambahkan teks di line yang baru
data.write('/n harus banyak laihan biar jago')
data.close()  # untuk membebaskn memori yang dipakai

print('================= Better and Best Practice ===========')

try:
  f = open ('./data.txt', mode = 'a', encoding = 'utf - 8')

finally:
  f.close()

# Best Practice
with open ('./data.txt', mode = 'a', encoding = 'utf - 8') as f:
  f.write('/n semangat belajar Python, biar hidup terus berkembang')
  f.write('/n Thare is no eevator to success, you gotta take the stair')