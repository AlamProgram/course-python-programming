

#============== Fungsi Parametrik ========================

def halo_dunia():
    var ="halo dunia....!"
    print(var)

halo_dunia()


#============== Fungsi Parametrik ========================
def halo_bro(nama):
    var  = f'halo bro {nama}, gimana kabar?'
    print(var)

halo_bro("nuril")

# bisa lebih dari 1 parameter

def halo_bro(nama, asal):
    var  = f'halo {nama}, habis dari {asal}?'
    print(var)

halo_bro("nuril", 'tangerang')

# bisa tidak urut 

def halo_bro(nama, asal):
    var  = f'halo {nama}, habis dari {asal}?'
    print(var)

halo_bro(asal = 'bandung', nama = 'desti')


# untuk parameter yang isinya gak cuma 1

def selamat_datang(*daftar_nama):  # tanda * menangggap variabel daftar_nama sebagai list
    var  = 'halo '
    for nama in daftar_nama:
        var += nama + ', '

    var += "welcome..!"
    print(var)

selamat_datang('nurul', 'siska', 'lukman', 'handi')

#============== Fungsi Anonim ========================

double  = lambda x: x * 2

print(double(3))

#============== Doc String ========================

def selamat_datang(nama):
    '''
    ini adalah fungsi untuk
    memunculkan nama yang telah disebutkan
    '''
    var  = f'halo, {nama}, welcome....'
    print(var)

selamat_datang('nurul')
print(selamat_datang.__doc__)

#============== Return ========================

def operasi(a, b, c = 1):
    op1 = a + b
    op2 = op1 // c

    return op2                  #hasil dari fungsi akan ditampung dalam 'hasil' 

hasil = operasi(a = 10, b = 5)
print(hasil)
    
    
#============== Scope ========================

a = 2
x = 100

def operasi(a, b, c = 1):
    op1 = a + b
    op2 = op1 // c

    print ('a di dalam function adalah ', a)
    print(x)                                    # nilai variabel yang diluar fungsi bisa diakses ke dalam fungsi, tapi tidak sebaliknya
    return op2                 

hasil = operasi(a = 10, b = 5)
print(hasil)

print("a di luar function", a)  # a yang di luar function berbeda dengan a di dalam function