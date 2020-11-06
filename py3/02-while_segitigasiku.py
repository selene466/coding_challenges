#!/usr/bin/python3
# soal:
# buat segitiga siku dengan perulangan while

panjang = input("Input bintang: ")

start = 1
sts = 0
while (start < int(panjang)):
  start += 1
  while (sts < start):
    sts += 1
    print("*" * sts)

