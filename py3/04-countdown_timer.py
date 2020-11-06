#!/usr/bin/python3
# soal by africode07:
# buat... program... hitung... mundur... ahahay

from time import time, sleep

def mclear():
  print("\n" * 100)

inp = input("Input waktu dalam second\n: ")
wkt = int(inp)

while (wkt >= 0):
  mclear()
  print(f"Countdown: {wkt}")
  if wkt == 0:
    print("Countdown selesai...")
  wkt = wkt - 1
  sleep(1)
