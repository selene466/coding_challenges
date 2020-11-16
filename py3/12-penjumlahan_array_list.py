#!/usr/bin/env python3
# Soal latihan sum array list
# Sebuah program perulangan digunakan untuk menghitung jumlah dari angka - angka pada suatu batas yang user inputkan.
# User bisa menginputkan angka awal, angka akhir, dan akhir bagi, seperti ini:
#
# ==========
# Masukkan batas awal   : 1
# Masukkan batas akhir  : 10
# Masukkan angka bagi   : 2
#
# Setelah user menginputkan ketiga hal tersebut, program akan menghitung jumlah total nilai dari batas awal sampai batas akhir.
# Tentukan:
# 1. Hasil penjumlahan dari batas awal sampai akhir
# 2. Hasil penjumlahan dibagi angka bagi
# 3. Nilai rata - rata dari data tersebut

def cekint(i):
  try:
    i = int(i)
    return i
  except ValueError:
    return i

print("=" * 10)
awal = cekint(input("Masukkan batas awal\t: "))
akhir = cekint(input("Masukkan batas akhir\t: "))
bagi = cekint(input("Masukkan angka bagi\t: "))

if awal > akhir:
  exit("Tidak valid")

#data = [i for i in range(awal, akhir)] # alternate, ref
data = [*range(awal, akhir)]
hasiljumlah = sum(data)
hasilbagi = hasiljumlah / bagi
hasilrata = hasiljumlah / len(data)

print(f"\nHasil jumlah\t: {hasiljumlah}")
print(f"Hasil bagi\t: {hasilbagi}")
print(f"Rata - rata\t: {hasilrata}")
