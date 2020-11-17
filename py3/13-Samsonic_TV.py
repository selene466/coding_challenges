#!/usr/bin/env python3
# Samsonic TV
# Soal:
# Televisi di Samsonic TV terdiri dari 100 channel (0 sampai dengan 99). Sayangnya walau memiliki banyak channel, Samsonic TV tidak mempunyai remote. Budi memiliki televisi produksi Samsonic TV. Namun, karena Budi tidak memiliki remote, maka dia harus memindahkan channel TV secara manual dengan menekan tombol naik dan turun. Dia menyadari bahwa jika channel sudah mencapai 99, dan dia menekan tombol naik, maka channel akan kembali ke nol. Begitupun sebaliknya, jika channel sudah di nol dan dia menekan tombol turun, maka channel akan menjadi 99.
# Karena Budi orang yang malas, dia selalu ingin meminimalkan penekanan tombol. Misalkan, jika channel awal adalah 2 dan channel tujuan adalah 95 maka dia akan memilih menekan tombol turun sebanyak 7 kali daripada dia menekan tombol naik sebanyak 93 kali. Namun sayang sekali, Budi tidak pandai berhitung.
# Bantulah Budi untuk membuat program yang menentukan jumlah minimal penekanan tombol serta tombol apa yang harus ditekan.

pos = 0
jarak_channel = 100
while True:
  print(f"Sekarang di channel {pos}")
  print("-" * 20)
  ch = input("Ch: ")
  try:
    ch = int(ch)
  except ValueError:
    break
  if ch <= (jarak_channel - 1):
    stepup = 0
    stepdown = 0
    while True:
      stepup += 1
      if ((pos + (stepup % jarak_channel)) % jarak_channel) == ch:
        break
    while True:
      stepdown += 1
      if ((pos - (stepdown % jarak_channel)) % jarak_channel ) == ch:
        break
    if stepup < stepdown:
      print(f"Naik {stepup} channel")
    elif stepup > stepdown:
      print(f"Turun {stepdown} channel")
    pos = ch
  else:
    print(f"Hanya ada {jarak_channel - jarak_channel} - {jarak_channel - 1} channel")
print("Terima kasih")
