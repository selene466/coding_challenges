#!/usr/bin/env python3
'''
Buatlah fungsi untuk mengembalikan hasil penjumlahan pada list nums yang nilainya lebih dari batas.

Contoh:
jumlah_batas([1,2,3,4,5,6], 2)

Output:
18

Penjelasan, yang lebih dari 2 adalah 3,4,5,6
3 + 4 + 5 + 6 = 18
  
  
Contoh:
jumlah_batas([10, 2, 23, 41, 15, 6], 200)

Output:
0

Penjelasan, tidak ada bilangan yang lebih dari 200, sehingga fungsi akan mengembalikan 0
'''

def jumlah_batas(arr, batas):
  hasil = []
  for a in arr:
    if a > batas:
      hasil.append(a)
  return sum(hasil)

print(jumlah_batas([1, 2, 3, 4, 5, 6], 2))
print(jumlah_batas([10, 2, 23, 41, 15, 6], 200))
print(jumlah_batas([10, 2, 23, 41, 15, 6], 20))
