#!/usr/bin/env python3
# Rook
# Soal:
# Pak Junairi sedang belajar bermain catur. Sayangnya, ia tidak terlalu ingat aturan permainan catur sehingga tidak tahu apakah perpindahan bidak yang ia lakukan sah atau tidak.
# Salah satu yang sering dilupakan oleh Pak Junairi adalah aturan benteng.
# Pergerakan bidak benteng pada catur dianggap sah jika perpindahannya sejajar horizontal atau vertikal.
# Perhatikan gambar berikut. Perpindahan yang sah ditandai dengan warna hijau (0 di ascii art).
#
# 8 | C C C C 0 C C C
# 7 | C C C C 0 C C C
# 6 | C C C C 0 C C C
# 5 | C C C C 0 C C C
# 4 | 0 0 0 0 B 0 0 0
# 3 | C C C C 0 C C C
# 2 | C C C C 0 C C C
# 1 | C C C C 0 C C C
#   x----------------
#     a b c d e f g h
#
# Jika X merupakan posisi bidak secara horizontal dan Y merupakan posisi bidak secara vertikal, tentukan apakah perpindahan bidak benteng dari X1Y1 ke X2Y2 sah!
# Jika sah, tentukan juga ke mana bidak tersebut berpindah, ke kanan, kiri, maju atau mundur (asumsikan bidak maju jika nilai Y membesar).
#
# Spesifikasi Input
# Program akan menerima input berupa empat buat bilangan bulat yang merupakan X, Y1, X2, Y2, yang dipisahkan oleh spasi.
#
# Spesifikasi Output
# Output berupa String dengan aturan sebagai berikut.
# - "Tidak sah" jika perpindahan tidak sah.
# - "Maju" jika bidak catur begerak ke arah depan posisi awal.
# - "Mundur" jika bidah catur bergerak ke arah belakang posisi awal.
# - "Kanan" jika bidak catur bergerak ke arah kanan posisi awal.
# - "Kiri" jika bidak catur bergerak ke arah kiri posisi awal.
#
# Contoh Input 1
# 2 3 4 5
# Contoh Input 2
# 2 3 2 5
#
# Contoh Output 1
# Tidak sah
# Contoh Output 2
# Maju

inp = input("Input: ").split(" ")
x1 = inp[0]
y1 = inp[1]
x2 = inp[2]
y2 = inp[3]

if (x1 == x2) and (y1 == y2):
  print("Tidak berpindah")
elif (x1 == x2) and (y1 > y2):
  print("Mundur")
elif (x1 == x2) and (y1 < y2):
  print("Maju")
elif (x1 > x2) and (y1 == y2):
  print("Kiri")
elif (x1 < x2) and (y1 == y2):
  print("Kanan")
else:
  print("Tidak sah")
