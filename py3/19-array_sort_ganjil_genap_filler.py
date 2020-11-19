#!/usr/bin/env python
# Soal:
#
# Contoh Data / Input 1
# 2, 1, 202, 77, 911, 40
# Contoh Data / Input 2
# 100, 11, 21, 5, 2020, 50
#
# Contoh Output 1
# 2   202        40
#   1     77 99    
# Contoh Output 2
# 100         2020 50
#     11 21 5        

inp = [2, 233, 150, 20]
inp = input("Data input: ").split(", ")

atas = []
bawah = []
for i in inp:
  filler = 0
  for x in range(len(i)):
    filler += 1
  try:
    i = int(i)
  except ValueError:
    exit("Bukan angka")
  if i % 2 == 0:
    atas.append(str(i))
    bawah.append(" " * filler)
  else:
    bawah.append(str(i))
    atas.append(" " * filler)

print(' '.join(atas))
print(' '.join(bawah))
