#!/usr/bin/env python3
'''
Buatlah program yang menerima N buah bilangan dan menuliskan kembali bilangan tersebut, namun terbalik

Contoh:
Masukkan nilai N: 5
5
2
1
6
3
Hasil dibalik:
3
6
1
2
5
'''

n = input('Masukkan nilai N: ')
inp = []
for n in range(int(n)):
  inp.append(input())

inp.reverse()
print('Hasil dibalik:')
for n in inp:
  print(n)
