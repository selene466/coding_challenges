#!/usr/bin/env python3
'''
1. Hitunglah gaji seorang pegawai dengan syarat sebagai berikut ini:
a. Gaji Pokok setiap Karyawan adalah 2.500.000
b. Tunjangan
  - Jika Karyawan masih lajang Tunjangannya Rp. 300.000
  - Jika Karyawan Kawin anak <= 2 Tunjangannya Rp. 500.000
  - Jika Karyawan Kawin anak >2 Tunjangannya Rp. 750.000
c. Biaya BPJS 4% dari (Gaji Pokok + Tunjangan)
d. Pajak PPh 21 dikenakan 5% dari (Gaji Pokok + Tunjangan)
e. Total Gaji = (Gaji Pokok + Tunjangan) - (Biaya BPJS - PPh 21)
'''

class Gaji(object):
  def __init__(self, nik, nama, status, anak):
    self.__nik = nik
    self.__nama = nama
    self.__status = status
    self.__anak = anak
    self.__gajipokok = 2500000

  def nikKaryawan(self):
    return self.__nik

  def namaKaryawan(self):
    return self.__nama

  def statusKaryawan(self):
    return self.__status

  def statusKaryawanTeks(self):
    if self.__status == 0:
      self.__teks = 'Lajang'
    elif self.__status == 1:
      self.__teks = 'Kawin'
    return self.__teks

  def anakKaryawan(self):
    return self.__anak

  def gajiPokok(self):
    return self.__gajipokok

  def Tunjangan(self):
    if __class__.statusKaryawan(self) == 0:
      tunjangan = 300000
    elif __class__.statusKaryawan(self) == 1 and __class__.anakKaryawan(self) <= 2:
      tunjangan = 500000
    elif __class__.statusKaryawan(self) == 1 and __class__.anakKaryawan(self) > 2:
      tunjangan = 750000
    return tunjangan

  def BPJS(self):
    return round((__class__.gajiPokok(self) + __class__.Tunjangan(self)) * 4 / 100)

  def pajakPPh21(self):
    return round((__class__.gajiPokok(self) + __class__.Tunjangan(self)) * 5 / 100)

  def totalGaji(self):
    return (__class__.gajiPokok(self) + __class__.Tunjangan(self)) - (__class__.BPJS(self) + __class__.pajakPPh21(self))
  
  
karyawan1 = Gaji(1234, 'Andrian', 1, 2)
print('=' * 80)
print('NIK\tNama\tStatus\tAnak\tGapok\tTunjangan\tBPJS\tPPh21\tTotal')
print(f'{karyawan1.nikKaryawan()}\t{karyawan1.namaKaryawan()}\t{karyawan1.statusKaryawanTeks()}\t{karyawan1.anakKaryawan()}\t{karyawan1.gajiPokok()}\t{karyawan1.Tunjangan()}\t\t{karyawan1.BPJS()}\t{karyawan1.pajakPPh21()}\t{karyawan1.totalGaji()}')
print('=' * 80)
