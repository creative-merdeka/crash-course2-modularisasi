"""
Program menghitung luas segitga
r l_s = a*t/2
"""

print('menghitung luas segitiga 1')
alas = 25
tinggi = 3
luas_segitiga = alas * tinggi / 2
print(f'segitiga dengan alas={alas} dan tinggi={tinggi} memiliki luas={luas_segitiga}')

print('\nmenghitung luas segitiga 2 dengan co-pas')
alas = 10
tinggi = 7
luas_segitiga = alas * tinggi / 2
print(f'segitiga dengan alas={alas} dan tinggi={tinggi} memiliki luas={luas_segitiga}')

# Definisi Fungsi
print('\nmembuat fungsi hitung_luas_segitiga')

def hitung_luas_segitiga(alas, tinggi) :  # => object untuk mendefinisikan item
    luas_segitiga = alas * tinggi / 2  # Exe yang akan di lakukan
    return luas_segitiga  # Dia akan kembali melakukan perintah

alas = 25
tinggi = 3
print(
    f'\nmenghitung luas segitiga dgn fungsi,'
    f'alas={alas} dan tinggi={tinggi}'
    f'hasilnya = {hitung_luas_segitiga(alas, tinggi)}'
      )

# ket cetak : f'-variab {masukan def(masukan nilai exe)'(komputer akan otomatis bekerja)
print(f'\nmenghitung luas segitiga dgn fungsi,hasilnya = {hitung_luas_segitiga(2, 7)}')
print(f'menghitung luas segitiga dgn fungsi,hasilnya = {hitung_luas_segitiga(10, 7)}')
print(f'menghitung luas segitiga dgn fungsi,hasilnya = {hitung_luas_segitiga(50, 3)}')

