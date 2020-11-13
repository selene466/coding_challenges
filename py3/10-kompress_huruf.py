#!/usr/bin/env python
# Soal:
# Sebuah lembaga pendidikan akan mengirim kunci jawaban peserta ke kantor pusat pendidikan tersebut.
# Hanya saja mereka menyadari bahwa ternyata filenya terlalu besar oleh karena itu mereka menggunakan penyederhanaan melalui ide kompressi data pada kunci jawaban tersebut.
#
# Aturan kompressi:
# Untuk setiap jawaban yang sama berturut-turut maka hanya akan ditulis satu kali dan angka yang menyatakan perulangan akan ditulis di depannya.
#
# Contoh:
# Input: aaaabbcccdd
# Output: 4a2b3c2d

def kompresshuruf(data):
  prevhuruf = data[:1]
  num = 1
  hasil = []
  for h in data[1:]:
    if h == prevhuruf:
      num += 1
    else:
      hasil.append(str(num) + prevhuruf)
      num = 1
      prevhuruf = h
  return ''.join(hasil) + str(num) + prevhuruf

strg = input("Input: ")
dt = kompresshuruf(strg)
print(f"Output: {dt}")
