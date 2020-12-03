#!/usr/bin/env python3
'''
3. Terdapat kumpulan bilangan array sebagai berikut:

2, 12, 15, 17, 35, 4, 51, 7, 13, 18, 27, 16, 46, 50, 43, 22

a. Tampilkan bilangan yang habis dibagi 3
b. Tampilkan bilangan genap
c. Tampilkan bilangan prima
'''

class Main:
  def aplikasi():
    tampil = Program()
    for a in tampil.tampilArr():
      print(a, end=' ')
    print()
    print('[1] Tampilkan bilangan yang habis dibagi 3')
    print('[2] Tampilkan bilangan genap')
    print('[3] Tampilkan bilangan prima')
    pil = input('Masukkan angka pilihan: ')
    try:
      pil = int(pil)
    except ValueError:
      exit('Bukan angka')
    if pil == 1:
      obj = Program()
      print(*obj.program_1(), sep=' ')
    elif pil == 2:
      obj = Program()
      print(*obj.program_2(), sep=' ')
    elif pil == 3:
      obj = Program()
      print(*obj.program_3(), sep=' ')
    else:
      exit('Pilihan tidak valid')
  
  
class Program:
  def __init__(self):
    self.arr = [2, 12, 15, 17, 35, 4, 51, 7, 13, 18, 27, 16, 46, 50, 43, 22]

  def tampilArr(self):
    return self.arr

  def program_1(self):
    out = []
    for a in self.arr:
      if a % 3 == 0:
        out.append(a)
    return out

  def program_2(self):
    out = []
    for a in self.arr:
      if a % 2 == 0:
        out.append(a)
    return out

  def program_3(self):
    out = []
    for a in self.arr:
      for i in range(2, a):
        if a % i == 0:
          break
      else:
        out.append(a)
    return out
  
  
if __name__ == '__main__':
  Main.aplikasi()
