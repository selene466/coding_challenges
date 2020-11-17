#!/usr/bin/env python3
# Rook
# Soal:
# Seorang Remaja sedang bingung untuk menentukan siapa saja diantara temannya yang merupakan teman dekatnya. Untuk itu ia menetapkan 3 level pertemanan.
# Level "Sangat bro!" merupakan level yang ditujukan kepada temannya yang memberikan ucapan ulang tahun pada tanggal yang benar dan paling lambat 2 jam setelah jam 12 malam.
# Level "Bro!" merupakan teman-temannya yang memberikan ucapan ulang tahun pada tanggal yang benar saja.
# Sedangkan level "Kurang bro!" merupakan teman-temannya yang memberikan ucapan ulang tahun pada tanggal yang salah.
#
# Spesifikasi Masukan
# Masukan program terdiri dari 3 buah bilangan bulat yaitu n, m, dan x. Bilangan n (0 <= n <= 23) merupakan jam temannya memberikan ucapan selamat ulang tahun
# Bilangan bulat m (1 <= m <= 31) merupakan tanggal temannya memberikan selamat ulang tanggal.
# Sedangkan bilangan bulat x (1 <= x <= 31) merupakan tanggal dimana seorang remaja berulang tahun.
#
# Spesifikasi Keluaran
# Keluarkan "Sangat bro!", "Bro!", atau "Kurang bro!" sesuai dengan deskripsi masalah
#
#
# Contoh Masukan 1
# 0 21 21
# Contoh Masukan 2
# 2 21 21
# Contoh Masukan 3
# 13 21 21
#
# Contoh Keluaran 1
# Sangat bro!
# Contoh Keluaran 2
# Sangat bro!
# Contoh Keluaran 3
# Bro!

inp = input("Input: ").split(" ")
n = int(inp[0])
m = int(inp[1])
x = int(inp[2])
if 0 <= n <= 23:
  if 1 <= m <= 31:
    if 1 <= x <= 31:
      if (m == x) and (n <= 2):
        print("Sangat bro!")
      elif (m == x) and (n > 2):
        print("Bro!")
      else:
        print("Kurang bro!")
    else:
      print("Tanggal tidak valid")
  else:
    print("Tanggal tidak valid")
else:
  print("Jam tidak valid")

