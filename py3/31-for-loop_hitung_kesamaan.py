#!/usr/bin/env python3
'''
Hitung Kesamaaan
Soal:
Buatlah program untuk menghitung jumlah kesamaan karakter dari dua kata!
'''

def hitung_kesamaan(kata1, kata2):
  sama = 0
  for huruf1 in kata1:
    for huruf2 in kata2:
      if huruf1 == huruf2:
        sama += 1
  return sama

kata1 = 'python'
kata2 = 'path'
print(kata1, kata2)
print('Kesamaan karakter:', hitung_kesamaan(kata1, kata2))
print()
kata1 = 'watame'
kata2 = 'korone'
print(kata1, kata2)
print('Kesamaan karakter:', hitung_kesamaan(kata1, kata2))
print()
kata1 = 'inugami'
kata2 = 'nekomata'
print(kata1, kata2)
print('Kesamaan karakter:', hitung_kesamaan(kata1, kata2))
