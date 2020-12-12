#!/usr/bin/env python3
'''
Soal:
Buatlah program untuk menampilkan bilangan Fibonacci sesuai dengan inputan user.
Jika diinput 10 maka akan muncul 10 bilangan Fibonacci dan seterusnya!
'''

n = input('Masukkan nilai N: ')
try:
  n = int(n)
except ValueError:
  exit('Input wajib bilangan bulat')

a = 0
b = 1
jml = 0
c = a + b
while (n > 0):
  print(jml, end=' ')
  a = b
  b = jml
  jml = a + b
  n -= 1
