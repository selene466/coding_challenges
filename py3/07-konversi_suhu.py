#!/usr/bin/env python
# Soal latihan membuat konversi suhu

celc = input("Input suhu dalam Celcius: ")

reamur = (4 / 5) * float(celc)
kelvin = float(celc) + 273.15
fahrenheit = (9 / 5) * float(celc) + 32

print(f"\nSuhu dalam satuan Reamur: {format(reamur, '.2f')}")
print(f"Suhu dalam satuan Kelvin: {format(kelvin, '.2f')}")
print(f"Suhu dalam satuan Fahrenheit: {format(fahrenheit, '.2f')}")
