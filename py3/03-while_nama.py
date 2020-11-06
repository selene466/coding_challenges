#!/usr/bin/python3
# soal:
# buat segitiga siku dengan perulangan while dari input nama

nama = input("Input nama: ")

start = 1
sts = 0
while (start < len(nama)):
  start += 1
  while (sts < start):
    sts += 1
    print(nama[:sts])
