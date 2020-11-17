#!/usr/bin/env python3
# Wukalapak
# Soal:
# Toko online Wukalapak sedang mengadakan promo dengan memberikan voucher belanja. Voucher tersebut memberikan diskon 10% terhadap biaya total belanja. Jika barang tidak dikirim melainkan pembeli mengambil sendiri ke gudang, maka penggunaan voucher akan memotong 20% dari harga barang.
# Namun voucher belanja tersebut memiliki keterbatasan, jika biaya pengiriman melebihi harga barang maka voucher hanya akan memotong 5% dari biaya pengiriman barang tanpa memotong harga barang.

# Berikut adalah perhitungan biaya total dan biaya pengiriman:
# biaya_total = harga_barang + biaya_pengiriman
# biaya_pengiriman = berat_barang * 2500
#
# Bantulah Mad Siri untuk menentukan uang yang harus dibayar oleh Mad Siri tersebut!
#
# Spesifikasi Masukan
# Masukan terdiri dari 2 buah bilangan bulat n dan m, dan sebuah string k.
# Bilangan bulat n merupakan harga barang yang akan dibeli Mad Siri.
# Sedangkan bilangan bulat m merupakan berat dari barang yang akan dibeli Mad Siri.
# String k merupakan string berniliai "dikirim" atau "diambil" yang menandakan jika barang yang dibeli Mad Siri akan dikirimkan oleh penjual atau diambil sendiri oleh pembeli.
#
# Spesifikasi Keluaran
# Uang yang harus dibayarkan oleh Mad Siri, dengan ketelitian 2 desimal di belakang koma.
#
# Contoh Masukan
# 12000 3 dikirim
#
# Contoh Keluaran
# 17550.00

inp = input("Input: ").split(" ")
harga_barang = int(inp[0])
berat_barang = int(inp[1])
metode = inp[2]

biaya_pengiriman = berat_barang * 2500
biaya_total = harga_barang + biaya_pengiriman

if metode == "dikirim":
  voucher = 10 / 100
  biaya_total = biaya_total - (biaya_total * voucher)
elif metode == "diambil":
  voucher = 20 / 100
  biaya_total = biaya_total - (biaya_total * voucher)
if biaya_pengiriman > harga_barang:
  voucher = 5 / 100
  biaya_total = harga_barang + (biaya_pengiriman - (biaya_pengiriman * voucher))

print(format(biaya_total, '.2f'))
