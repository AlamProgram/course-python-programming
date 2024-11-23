

# lanjut menit 2.19 
import re

teks = 'regex'
teks2 = 'redex'
x = re.match('^r...x$', teks2)      #^r  = dimulai dengan r; ... bebas 3 huruf; x$ = diakhiri x
print(x)

teks = "saya senang belajar regex"
x = re.split("\s", teks)            # /s = split kata yang memuat spasi
print(x)

teks =  '''
        ada 3 tipe loop, atau perlulangan di python yaitu, While loop, For loop
        dan nasted loop 2022
        '''
x = re.sub('\d+','--', teks )         # \d  = string memuat angka 0-9; +  = satu atau lebih keberadaan

print(x)
# lanjut 9.36

print('======================================')

teks = "hujan deras di kawasan depok"
x = re.search('^hujan.*depok$', teks)                        # diawali dengan hujan, * karakter apapun, $ diakhiri dengan # bisa pakai .serch atau .match

if x:
    print(" kata match")
else:
    print('kata tidak match')
    
print('======================================')

teks = "20 nov 2024 20 November '24 20/11/2024 20.11.2024"
x= re.findall('\d{2} [a-z]{3} \d{4}', teks)
print(x)

print('======================================')



teks = 'harga 1 mobil antik $1000'
x = re.sub('\$\d+', '_', teks)                  #\$ diawali dolar, \d+ diteruskan dengan digit bebas
print(x)

print('======================================')

teks = "akan dialihkan ke http://IndonesiaAI.com"
x = re.sub("http[s]?\://\S+",' ', teks)             # diawali dengan http, s opsional: dilanjutkan dengan karakter apapun; dilanjutkan 
print(x)

print('======================================')
teks = 'luar biasa banyak anak muda yang treveling tahun ini, begini tanggapan Lesti #trevel #_lesti #viral #gadget'
x = re.findall('#[_]*[a-z]+', teks)
print(x)
