#!/usr/bin/env python
# Soal:
# Buatlah program untuk menampilkan tiga huruf terdepan nama anda
# Misal nama anda AGUS, maka buatlah tampilan seperti berikut
#
# AAAAAAA         GGGGGGGGG        UU    UU
# AAAAAAA         GGGGGGGGG        UU    UU
# AA   AA         GG               UU    UU
# AA   AA         GG  GGGGGG       UU    UU
# AAAAAAA         GG  GGGGGG       UU    UU
# AA   AA         GG    GG         UU    UU
# AA   AA         GGGGGGGGG        UU    UU
# AA   AA         GGGGGGGGG        UUUUUUUU
#
# Done with python & for loop

def ascii_art(huruf):
  if huruf == "A":
    art = [' AA  ', 'A  A ', 'AAAA ', 'A  A ', 'A  A ', '    ']
  elif huruf == "B":
    art = ['BBBB  ', 'B   B ', 'BBBB  ', 'B   B ', 'BBBB  ', '     ']
  elif huruf == "C":
    art = [' CCC ', 'C    ', 'C    ', 'C    ', ' CCC ', '    ']
  elif huruf == "D":
    art = ['DDD  ', 'D  D ', 'D  D ', 'D  D ', 'DDD  ', '    ']
  elif huruf == "E":
    art = ['EEEE ', 'E    ', 'EEEE ', 'E    ', 'EEEE ', '    ']
  elif huruf == "F":
    art = ['FFFF ', 'F    ', 'FFF  ', 'F    ', 'F    ', '    ']
  elif huruf == "G":
    art = [' GGG  ', 'G     ', 'G  GG ', 'G   G ', ' GGG  ', '     ']
  elif huruf == "H":
    art = ['H  H ', 'H  H ', 'HHHH ', 'H  H ', 'H  H ', '    ']
  elif huruf == "I":
    art = ['III ', ' I  ', ' I  ', ' I  ', 'III ', '   ']
  elif huruf == "J":
    art = ['    J ', '    J ', '    J ', 'J   J ', ' JJJ  ', '     ']
  elif huruf == "K":
    art = ['K  K ', 'K K  ', 'KK   ', 'K K  ', 'K  K ', '    ']
  elif huruf == "L":
    art = ['L    ', 'L    ', 'L    ', 'L    ', 'LLLL ', '    ']
  elif huruf == "M":
    art = ['M   M ', 'MM MM ', 'M M M ', 'M   M ', 'M   M ', '     ']
  elif huruf == "N":
    art = ['N   N ', 'NN  N ', 'N N N ', 'N  NN ', 'N   N ', '     ']
  elif huruf == "O":
    art = [' OOO  ', 'O   O ', 'O   O ', 'O   O ', ' OOO  ', '     ']
  elif huruf == "P":
    art = ['PPPP  ', 'P   P ', 'PPPP  ', 'P     ', 'P     ', '     ']
  elif huruf == "Q":
    art = [' QQQ  ', 'Q   Q ', 'Q   Q ', 'Q  QQ ', ' QQQQ ', '     Q']
  elif huruf == "R":
    art = ['RRRR  ', 'R   R ', 'RRRR  ', 'R R   ', 'R  RR ', '      ']
  elif huruf == "S":
    art = [' SSS  ', 'S     ', ' SSS  ', '    S ', 'SSSS  ', '      ']
  elif huruf == "T":
    art = ['TTTTTT ', '  TT   ', '  TT   ', '  TT   ', '  TT   ', '       ']
  elif huruf == "U":
    art = ['U   U ', 'U   U ', 'U   U ', 'U   U ', ' UUU  ', '      ']
  elif huruf == "V":
    art = ['V     V ', 'V     V ', ' V   V  ', '  V V   ', '   V    ', '        ']
  elif huruf == "W":
    art = ['W     W ', 'W     W ', 'W  W  W ', ' W W W  ', '  W W   ', '        ']
  elif huruf == "X":
    art = ['X   X ', ' X X  ', '  X   ', ' X X  ', 'X   X ', '      ']
  elif huruf == "Y":
    art = ['Y   Y ', ' Y Y  ', '  Y   ', '  Y   ', '  Y   ', '      ']
  elif huruf == "Z":
    art = ['ZZZZZ ', '   Z  ', '  Z   ', '  Z   ', 'ZZZZZ ', '      ']
  return art

nama = input("Input nama: ").upper()
namacut = nama[:3]
data = []
for hrf in namacut:
  data.append(ascii_art(hrf))

joinhrf = list(map(''.join, zip(*data))) # thx https://stackoverflow.com/a/56479940
for i in range(6):
  print(joinhrf[i])

