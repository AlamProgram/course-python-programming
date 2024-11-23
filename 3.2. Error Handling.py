
# Syantax Error
fruit_list = ['apple', 'banana', 'watermelon']

for fruit in fruit_list
  print(fruit)

# Logical Error
nilai = 10
pembagi = 0
hasil = nilai / pembagi
print(hasil)

# jenis error yang dikenaly Python
print(dir(locals()['__builtins__']))

# Solusi Agar Tidak Error

try:                            # karena kode eerror mak langsung ke exept
  nilai = 10
  pembagi = 0
  hasil = nilai / pembagi
  print(hasil)

except:
  print('ada yang error')


print('=============================================')

try:
  nilai = 10
  pembagi = 0
  hasil = nilai / pembagi
  print(hasil)

except Exception as e:
  print('Oops...! telah terjadi', e.__class__, '.')


print('================ Metode Lain ===================')


try:
  nilai = 10
  pembagi = 0
  hasil = nilai / pembagi
  print(hasil)

except ZeroDivisionError:
  print('Oooops, telah  terjadi ZeroDivisionError')

except ValueError:
  print('Oops, telah terjadi ValueError')

except:
  print('telah terjadi error yang tidak dikenali')

# Membua Error Sendiri

class ValueTooSmallError(Exception):
  pass

class ValueTooLargeError(Exception):
  pass

number = 10
while True:
  try:
    i_num = int(input('masukkan angka anda ' ))
    if i_num > number:
      raise ValueTooLargeError
    elif i_num < number:
      raise ValueTooSmallError
    elif i_num == number:
      True
      break

  except ValueTooSmallError:
    print('nilai terlalu kecil')
    print(' ')
  except ValueTooLargeError:
    print('nilai terlalu besar')
    print(' ')

print('angka yang kamu tebak benar')

