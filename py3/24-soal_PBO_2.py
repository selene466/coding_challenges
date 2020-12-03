#!/usr/bin/env python3
'''
2. Ada sebuah deret pola sebagai berikut:

2/3 - 3/9 + 4/27 - 5/81 + 6/243 ......

Buatlah aplikasi untuk menentukan suku ke n
'''

class Main:
  def aplikasi():
    n = input('Masukkan nilai n: ')
    try:
      n = int(n)
    except ValueError:
      exit('n bukan bilangan bulat')
    obj = Program(n)
    obj.program()
  
  
class Program:
  def __init__(self, n):
    self.n = n

  def program(self):
    n = self.n
    indexA = 1
    indexB = 1
    for i in range(n):
      indexA += 1
      indexB *= 3
      print(f'{indexA}/{indexB}', end='')
      if indexA <= n:
        if i % 2 == 0:
          print(' - ', end='')
        else:
          print(' + ', end='')
  
  
if __name__ == '__main__':
  Main.aplikasi()
