#!/usr/bin/env python3
'''
Soal Bingkai Angka:
Contoh Input
6

Contoh Output
01 02 03 04 05 06
20             07
19             08
18             09
17             10
16 15 14 13 12 11

Contoh Input
5

Contoh Output
01 02 03 04 05
16          06
15          07
14          08
13 12 11 10 09
'''

inp = input('')
try:
  inp = int(inp)
except ValueError:
  exit('bukan angka')
for i in range(inp):
  i += 1
  for j in range(inp):
    j += 1
    if i == 1:
      print(f'{j:02d}', end=' ')
    elif i < inp:
      if j == 1:
        print(f'{inp * 4 - i - 2:02d}', end=' ')
      elif j == inp:
        print(f'{inp + i - 1:02d}', end=' ')
      else:
        print('  ', end=' ')
    else:
      if j == 1:
        print(f'{inp + i * 2 - 2:02d}', end=' ')
      if j == inp:
        print(f'{inp + j - 1:02d}', end=' ')
      elif 1 < j < inp:
        print(f'{inp + i * 2 - j - 1:02d}', end=' ')
  print()
