#!/usr/bin/env python3
# Samsonic Calendar
# Soal:
# Di Pulai Beringin terdapat suatu perusahaan percetakan kalender. Pak Sakir, sang pemilik perusahaan selalu kebingungan jika akan mencetak bulan Februari, apakah hanya 28 hari atau 29 hari.
# Jika tahun yang bersangkutan adalah tahun kabisat, maka bulan Februari memiliki 29 hari.
# Jika bukan kabisat maka 28 hari.
# Berikut ketentuan tahun kabisat:
# - Jika tidak habis dibagi 4: bukan kabisat
# - Jika habis dibagi 4 dan tidak habis dibagi 100: kabisat
# - Jika habis dibagi 4 dan habis dibagi 100, tetapi tidak habis dibagi 400: bukan kabisat
#   Selain ketentuan di atas, semuanya termasuk tahun kabisat
#
# Bantulah Pak Sakir untuk menentukan tahun yang akan dicetak kabisat atau bukan.
#
#
# Spesifikasi Input:
# Program akan menerima input berupa bilangan bulat yang merupakan tahun yang akan dicetak.
#
# Spesifikasi Output:
# Output berupa String, "Kabisat" jika tahun input adalah tahun kabisat, atau "Bukan kabisat" jika tahun input bukan tahun kabisat.
#
# Contoh Input 1
# 1800
# Contoh Input 2
# 1600
#
# Contoh Output 1
# Bukan kabisat
# Contoh Output 2
# Kabisat


tahun = input("Masukan Tahun: ")
try:
 tahun = int(tahun)
except ValueError:
 print("Bukan angka")
 exit()

if tahun % 4 == 0:
  if tahun % 100 == 0:
    if tahun % 400 == 0:
      print("Tahun kabisat")
    else:
      print("Bukan kabisat")
  else:
    print("Tahun Kabisat")
else:
  print("Bukan kabisat")
