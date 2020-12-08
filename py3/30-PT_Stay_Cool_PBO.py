#!/usr/bin/env python3
'''
Soal:
PT. STAY COOL, Memberikan Honor tetap kepada karyawan kontraknya sebesar Rp 700,000,- per bulan dengan memperoleh tunjangan-tunjangan sebagai berikut:

> Tunjangan Jabatan:
Golongan     Persentase
   1             5%
   2            10%
   3            15%

> Honor Lembur jumlah jam kerja normal dalam satu bulan sebanyak 240 Jam Kerja. Honor lembur diberikan jika jumlah jam kerja lebih dari 240 jam, maka kelebihan jam kerja tersebut dikalikan dengan honor lembur perjam sebesar Rp 2,500,- untuk setiap kelebihan jam kerja dalam satu bulannya.

> Pendapatan Bersih = Honor tetap + Tunjangan jabatan + Honor lembur - Pajak 10%

> Total gaji yang dikeluarkan = akumulasi dari pendapatan bersih karyawan

> Tampilan yang diinginkan sebagai berikut:

Layar Masukkan dan Keluaran

Program Hitung Honor Karyawan Kontrak
PT. STAY COOL

Masukkan Jumlah Karyawan: ...<input>
Karyawan Ke = ...<counter>
Nama Karyawan: ...<input>
Golongan (1/2/3): ...<input>
Jumlah Jam Kerja: ...<input>

<<Terus berulan tergantung Jumlah Karyawan>>



-----------------------------------------------------------
No. Nama        Tunjangan    Honor     Pajak    Pendapatan
    Karyawan    Jabatan      Lembur             Bersih
-----------------------------------------------------------
..  ........    .........    ......    .....    ..........
..  ........    .........    ......    .....    ..........
-----------------------------------------------------------
                     Total Gaji yang dikeluarkan Rp. .....



'''

from shutil import get_terminal_size

kolomlayar = get_terminal_size().columns

class Karyawan:
  daftar = []
  def __init__(self, nama, golongan, jam_kerja):
    self.__nama = nama
    self.__golongan = golongan
    self.__jam_kerja = jam_kerja - 240
    self.__honor_tetap = 700000
    self.__class__.daftar.append(self)

  def karyawanNama(self):
    return self.__nama

  def tunjanganJabatan(self):
    if self.__golongan == 1:
      persentase = 0.05
    elif self.__golongan == 2:
      persentase = 0.1
    else:
      persentase = 0.15
    tunjangan = self.__honor_tetap * persentase
    return round(tunjangan)

  def honorLembur(self):
    if self.__jam_kerja > 0:
      honor = self.__jam_kerja * 2500
    else:
      honor = 0
    return round(honor)

  def pajak(self):
    return round((self.__honor_tetap + __class__.tunjanganJabatan(self) + __class__.honorLembur(self)) * 0.1)

  def pendapatanBersih(self):
    return round(self.__honor_tetap + __class__.tunjanganJabatan(self) + __class__.honorLembur(self) - __class__.pajak(self))
  
  
class daftarKaryawan(Karyawan):
  def __init__(self):
    self.daftar = super().daftar
  
  
  
  
if __name__ == '__main__':
  print('\n' * 100)
  print('Program Hitung Karyawan Kontrak')
  print('PT. STAY COOL')
  print()
  jml_karyawan = input('Masukkan Jumlah Karyawan: ')
  try:
    jml_karyawan = int(jml_karyawan)
  except ValueError:
    exit('Jumlah bukan bilangan bulat')
  for karyawan in range(jml_karyawan):
    karyawan += 1
    print('Karyawan Ke -', karyawan)
    nama = input('Nama Karyawan: ')
    golongan = input('Golongan (1/2/3): ')
    try:
      golongan = int(golongan)
    except ValueError:
      exit('Input tidak valid')
    jam_kerja = input('Jumlah Jam Kerja: ')
    try:
      jam_kerja = int(jam_kerja)
    except ValueError:
      exit('Input tidak valid')
    Karyawan(nama, golongan, jam_kerja)
    print()

  print('\n' * 100)
  print('PT. STAY COOL'.center(kolomlayar))
  print('-' * kolomlayar)
  print('No.\tNama\t\tTunjangan')
  print('\tKaryawan\tJabatan\t\tHonor\t\t\t\tPendapatan')
  print('\t\t\t\t\tLembur\t\tPajak\t\tBersih')
  print('-' * kolomlayar)
  counter = 0
  total = []
  for k in daftarKaryawan().daftar:
    counter += 1
    print(f'{counter:>3}. {k.karyawanNama():>15}\t{k.tunjanganJabatan():>12,}\t{k.honorLembur():>12,}\t{k.pajak():>12,}\t{k.pendapatanBersih():>12,}')
    total.append(k.pendapatanBersih())
  print('-' * kolomlayar)
  print(f'\t\t\t\t\tTotal Gaji yang dikeluarkan Rp. {sum(total):>12,}')
