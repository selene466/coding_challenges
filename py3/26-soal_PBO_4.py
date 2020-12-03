#!/usr/bin/env python3
'''
4. Buatlah Aplikasi untuk membuat tanda silang berikut:

N = 5   N = 7     N = 9
@===@   @=====@   @=======@
=@=@=   =@===@=   =@=====@=
==@==   ==@=@==   ==@===@==
=@=@=   ===@===   ===@=@===
@===@   ==@=@==   ====@====
        =@===@=   ===@=@===
        @=====@   ==@===@==
                  =@=====@=
                  @=======@
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
    for i in range(n):
      for j in range(n):
        if i == min(range(n)) or i == max(range(n)):
          if j == min(range(n)) or j == max(range(n)):
            print('@', end='')
          else:
            print('=', end='')
        elif j == i:
          print('@', end='')
        elif i == n - j - 1:
          print('@', end='')
        else:
          print('=', end='')
      print()
  
  
if __name__ == '__main__':
  Main.aplikasi()
