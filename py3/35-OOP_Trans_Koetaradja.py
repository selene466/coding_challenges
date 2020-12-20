#!/usr/bin/env python3
'''
Soal:
    Alkisah, anda merupakan seorang programmer handal di kota Banda Aceh. Karena anda sangat mahir dalam merancang program, pemerintah kota Banda Aceh meminta bantuan anda membuat program sederhana untuk mengelola penumpang di bus Trans Koetaradja. Karena imbalan yang ditawarkan pemkot sangat besar, anda pun menyetujui untuk mengambil projek tersebut.

    Kemudian anda mulai melakukan observasi tentang bus Trans Koetaradja. Berikut merupakan data dan fakta yang anda kumpulkan seputar Bus Trans Koetaradja:
    1. Bus hanya memiliki kursi penumpang, yang terdiri dari 4 kursi penumpang biasa dan 2 kursi prioritas.
    2. Kursi prioritas hanya dapat diisi oleh orang-orang berikut:
        > Lansia: umur lebih dari 60 tahun
        > Anak-anak: umu kurang dari 10 tahun
        > Ibu hamil
    3. Penumpang biasa dilarang duduk di kursi prioritas.
    4. Penumpang tidak bisa lagi menaiki bus jika bus sudah penuh

# solved dengan python, banyak junk method dibawah saya biarkan
'''

class Main:
  def Aplikasi():
    print('MENU:')
    print('[1] Naikkan Penumpang')
    print('[2] Turunkan Penumpang')
    print('[3] Lihat Penumpang')
    print('[0] Keluar')
    print()
    pil = input('Pilihan: ')
    try:
      pil = int(pil)
    except ValueError:
      input('Pilihan tidak valid, [enter]')
    if pil == 1:
      __class__.tambahPenumpang()
      print()
      __class__.kursiPenumpang()
    elif pil == 2:
      __class__.turunPenumpang()
      print()
      __class__.kursiPenumpang()
    elif pil == 3:
      __class__.kursiPenumpang()
    elif pil == 0:
      if Bus(Penumpang).getJumlahPenumpang() == 0:
        exit('Terima kasih')
      else:
        input('Masih ada penumpang, [enter]')
    else:
      print('Pilihan tidak valid!')

  def tambahPenumpang():
    if Bus(Penumpang).naikPenumpang():
      input('Penumpang berhasil ditambahkan! [enter]')
    else:
      input('Penumpang gagal ditambahkan! [enter]')

  def turunPenumpang():
    if Bus(Penumpang).turunkanPenumpang():
      input('Penumpang berhasil turun! [enter]')
    else:
      input('Penumpang tidak ditemukan! [enter]')

  def kursiPenumpang():
    if len(Bus(Penumpang).getPenumpangBiasa()) == 0:
      getPenumpangBiasa = '<kosong>'
    else:
      getPenumpangBiasa = ', '.join(Bus(Penumpang).getPenumpangBiasa())
    print('Penumpang Biasa:', getPenumpangBiasa)
    if len(Bus(Penumpang).getPenumpangPrioritas()) == 0:
      getPenumpangPrioritas = '<kosong>'
    else:
      getPenumpangPrioritas = ', '.join(Bus(Penumpang).getPenumpangPrioritas())
    print('Penumpang Prioritas:', getPenumpangPrioritas)
    print('Jumlah Penumpang:', Bus(Penumpang).getJumlahPenumpang())
    input('Tekan [enter]')
  
  
class Penumpang:
  penumpang = []
  def __init__(self, nama, umur, hamil):
    self.__nama = nama
    self.__umur = umur
    self.__hamil = hamil
    self.__class__.penumpang.append(self)

  def getNama(self):
    return str(self.__nama)

  def getUmur(self):
    return int(self.__umur)

  def getHamil(self):
    return self.__hamil
  
  
class Bus:
  def __init__(self, Penumpang):
    self.__data_penumpang = Penumpang.penumpang
    self.__jml_kursi_biasa = 4
    self.__jml_kursi_prioritas = 2
    self.__kursi_biasa = []
    self.__kursi_prioritas = []
    for d in self.__data_penumpang:
      if d.getUmur() <= 10 or d.getUmur() >= 60 or d.getHamil():
        if len(self.__kursi_prioritas) < self.__jml_kursi_prioritas:
          self.__kursi_prioritas.append(d.getNama())
        else:
          self.__kursi_biasa.append(d.getNama())
      else:
        self.__kursi_biasa.append(d.getNama())

  def getPenumpangBiasa(self):
    return self.__kursi_biasa

  def getJumlahPenumpangBiasa(self):
    return len(__class__.getPenumpangBiasa)

  def getPenumpangPrioritas(self):
    return self.__kursi_prioritas

  def getJumlahPenumpangPrioritas(self):
    return len(__class__.getPenumpangPrioritas)

  def getPenumpang(self):
    index = 0
    for p in self.__data_penumpang:
      index += 1
      print(str(index) + '.', p.getNama())

  def getJumlahPenumpang(self):
    return len(self.__data_penumpang)

  def naikPenumpang(self):
    if __class__.getJumlahPenumpang(self) < self.__jml_kursi_prioritas + self.__jml_kursi_biasa:
      nama = input('Nama\t: ')
      if not nama:
        return None
      umur = input('Umur\t: ')
      try:
        umur = int(umur)
      except ValueError:
        input('Umur bukan angka')
        return None
      hamil = input('Hamil (y/n) : ').lower()
      if hamil == 'y':
        hamil = True
      else:
        hamil = False
      Penumpang(nama, umur, hamil)
      return True
    else:
      return False

  def turunkanPenumpang(self):
    nama = input('Masukkan nama penumpang: ')
    status = 0
    temp = Penumpang.penumpang
    Penumpang.penumpang = []
    for p in temp:
      if nama == p.getNama():
        del p
        status = 1
      else:
        Penumpang.penumpang.append(p)
    if bool(status):
      return True
    else:
      return False

if __name__ == '__main__':
  print('\n' * 100)
  print('===== BUS TRANS KOETARADJA =====')
  while True:
    Main.Aplikasi()
    print('================================')
