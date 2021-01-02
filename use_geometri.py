"""
Fungsi Import dari file yang berbeda
"""

# cara baca >> dari fold geom .segi(file) import fungsinya
from geometry.segitiga import hitung_luas_segitiga  # cara pajng dan strukt pycharm
print(f'\nhitung luas segitiga = {hitung_luas_segitiga(10, 25)}')

import geometry.segitiga as gs  # cara menggunakan alias
print(f'\nmenggunakan alias,hitung luas segitiga = {gs.hitung_luas_segitiga(20, 11)}')
