#!/usr/bin/env python3
# Soal:
# Buatlah program dengan bentuk angka NIM terakhir kalian, misalnya 036:
# Outputnya
#
# Masukan size: 6
# xxxxxxx
# x     x
# x     x
# x     x
# x     x
# x     x
# xxxxxxx
# hhhhhhh
#       x
#       x
# hhhhhhh
#       n
#       n
# hhhhhhh
# xxxxxxx
# x      
# x      
# xxxxxxx
# x     x
# x     x
# xxxxxxx

from math import ceil

size = input("Masukkan size: ")
try:
  size = int(size)
except ValueError:
  exit("Bukan angka")


if size < 5:
  exit("Minimal 5")

if size % 2 == 0:
  size = size + 1

jarak = range(size) # Misal NIM terakhir = 039

for j in jarak:
  data = []
  for k in jarak:
    if j == min(jarak) or j == max(jarak):
      data.append("x")
    elif j < max(jarak):
      if k == min(jarak) or k == max(jarak):
        data.append("x")
      else:
        data.append(" ")
  print(''.join(data))

for j in jarak:
  data = []
  for k in jarak:
    if j == min(jarak) or j == max(jarak):
      data.append("h")
    elif j < max(jarak):
      if j < (ceil(size / 2)):
        if j < (ceil(size / 2) - 1):
          if k == max(jarak):
            data.append("x")
          else:
            data.append(" ")
        else:
          data.append("h")
      elif k > (ceil(size / 2) - 1):
        if k == max(jarak):
          data.append("n")
        else:
          data.append(" ")
      else:
        data.append(" ")
  print(''.join(data))

for j in jarak:
  data = []
  for k in jarak:
    if j == min(jarak) or j == max(jarak):
      data.append("x")
    elif j < max(jarak):
      if j < (ceil(size / 2)):
        if j < (ceil(size / 2) - 1):
          if k == min(jarak) or k == max(jarak):
            data.append("x")
          else:
            data.append(" ")
        else:
          data.append("x")
      elif k > (ceil(size / 2) - 1):
        if k == max(jarak):
          data.append("x")
        else:
          data.append(" ")
      else:
        data.append(" ")
  print(''.join(data))
