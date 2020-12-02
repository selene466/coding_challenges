#!/usr/bin/env python3
'''
Sebuah perusahaan angkutan PO. Harapan Lancar Semarang memiliki ketentuan harga tiket sebagai berikut:
Tujuan      Eksekutif       Bisnis      Ekonomi
Jakarta     350.000         250.000     150.000
Surabaya    365.000         300.000     150.000
Bandung     300.000         250.000     135.000

Dikarenakan dalam masa promosi maka khusus untuk tujuan Surabaya Ekonomi atau Bandung Eksekutif akan mendapatkan diskon 10%.

Buatlah program untuk menghitung jumlah pembayaran tiket dengan ketentuan:
Input: Kota tujuan, Kelas, Banyaknya tiket
Proses: Banyaknya tiket * harga
Output: Kota tujuan, Banyaknya tiket, Jumlah bayar, Discount, Total bayar
'''

class Tiket:
  def __init__(self, tujuan, tarif_eksekutif, tarif_bisnis, tarif_ekonomi):
    self.__tujuan = tujuan
    self.__tarif_eksekutif = tarif_eksekutif
    self.__tarif_bisnis = tarif_bisnis
    self.__tarif_ekonomi = tarif_ekonomi

  def Tujuan(self):
    return self.__tujuan

  def tarifEksekutif(self):
    return self.__tarif_eksekutif

  def tarifBisnis(self):
    return self.__tarif_bisnis

  def tarifEkonomi(self):
    return self.__tarif_ekonomi

  def tarifSemua(self):
    return [__class__.tarifEksekutif(self), __class__.tarifBisnis(self), __class__.tarifEkonomi(self)]
  
  
def cekint(i):
  try:
    i = int(i)
    return i
  except ValueError:
    exit('Input bukan angka')


TiketList = []
jakarta = Tiket('Jakarta', 350000, 250000, 150000)
surabaya = Tiket('Surabaya', 365000, 300000, 180000)
bandung = Tiket('Bandung', 300000, 250000, 135000)
TiketList.append(jakarta)
TiketList.append(surabaya)
TiketList.append(bandung)

print('\n' * 100)
print('*' * 20)
print('Pembelian tiket\nPO. Harapan Lancar Semarang')
print('*' * 20)
index = 0
for i in TiketList:
  index += 1
  print(f'{index:>3}. {i.Tujuan()}')
tujuan = cekint(input('Input nomor tujuan: ')) - 1
print(f'Tujuan: {TiketList[tujuan].Tujuan()}')
print(f'  1. Eksekutif {TiketList[tujuan].tarifEksekutif():>10,}')
print(f'  2. Bisnis    {TiketList[tujuan].tarifBisnis():>10,}')
print(f'  3. Ekonomi   {TiketList[tujuan].tarifEkonomi():>10,}')
kelas = cekint(input('Input nomor kelas: ')) - 1
harga = TiketList[tujuan].tarifSemua()[kelas]
jml_tiket = cekint(input('Banyaknya tiket: '))
bayar = jml_tiket * harga
if tujuan == 1 and kelas == 2:
  diskon = 10                # diskon surabaya & kelas ekonomi
elif tujuan == 2 and kelas == 0:
  diskon = 10                # diskon bandung & kelas eksekutif
else:
  diskon = 0
potongan_diskon = bayar * (diskon / 100)
total_bayar = bayar - round(potongan_diskon)
print('*' * 20)
print(f'Kota tujuan\t: {TiketList[tujuan].Tujuan()}')
print(f'Banyaknya tiket\t: {jml_tiket}')
print(f'Jumlah bayar\t: {bayar:>12,}')
print(f'Discount\t: {round(potongan_diskon):>12,}')
print(f'Total bayar\t: {round(total_bayar):>12,}')
