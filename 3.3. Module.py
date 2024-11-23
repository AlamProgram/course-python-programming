
# Module

#import playlist as pl

#playlist.play('digimon - butterfly')
#playlist.pause('digimon - butterfly')

print('================== as =======================')

import playlist as pl           # Penyingkatan


pl.play('Naruto - Flow')        # bisa untuk menjalankan fungsi dari file lain



print(pl.GENDRE)                              # bisa juga Memanggil variabel

from playlist import GENDRE, DURATION, TYPE   # hanya memanggi beberapa variabel atau fungsi

print(TYPE)

# from playlist import *                       # ngeload semua

#===================================

# Di python juga udah ada module2 yang sudah Build in (siap pakai)


import os
import math

from math import pi
from math import pi, e
from math import *

print("Nilai pi adalah", math.pi)

# Check ready-to-use method
# math

import sys
print(sys.path)



