#!/usr/bin/env python
# Soal:
# Buat array 2 dimensi dengan bentuk secara otomatis
# Jika dientri data melalui keyboard untuk ukuran matrik misal 4 atau 5 atau 6 dst
# Maka bentuk matrik otomatis seperti berikut:
#
# 1001           10001        100001
# 1101           11001        110001
# 1011           10101        101001
# 1001           10011        100101
#                10001        100011
#                             100001
# input = 4     input = 5     input = 6

n = input("Input: ")
data1 = []
num = 0
for i in range(int(n)):
  data2 = []
  for j in range(int(n)):
    if j == min(range(int(n))):
      data2.append("1")
    elif j == max(range(int(n))):
      data2.append("1")
    else:
      if j == num:
        data2.append("1")
      else:
        data2.append("0")
  data1.append(data2)
  num += 1

for d in data1: # output
  print(''.join(d))
