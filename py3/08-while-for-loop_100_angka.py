#!/usr/bin/env python
# Soal:
# Buatlah program untuk mencetak angka 1 sampai 100 dengan menggunakan perulangan.
# Angka dicetak per 10 kolom dan 10 baris, pada baris pertama jika angka sudah dicetak 10 kolom maka dilakukan pergantian baris.
# Jika sudah 10 baris maka ditampilkan pesan "Tekan enter untuk melanjutkan"
# Begitu seterusnya sampai angka ke 1000.

data = []
v = 100
while (v <= 1000):
  for i in range(v):
    i += 1
    data.append(i)

  for x in data:
    print(x, end="\t")
    if (x % 10 == 0):
      print("\n")
  v += 100
  input("Tekan enter untuk melanjutkan")

input("Sudah mencapai 1000")
