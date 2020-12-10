#!/usr/bin/env python3
'''
Your Weight On the Moon
Soal:
If you were standing on the moon right now, your weight would be 16,5 percent of what it is on Earth. You can calculate that by multiplying your Earth weight by 0,165.

If you gained a kilo in weight every year for the next 15 years, what would your weight be when you visited the moon each year and at the end of the 15 years?

Write a program using a for loop that prints your moon weight for each year.
'''

weight = input('Enter your weight in kilogram: ')
try:
  weight = int(weight)
except ValueError:
  exit('Youre entered invalid number')

weight_on_moon = weight * 0.165
weight_every_year = 1 * 0.165

index = 0
for y in range(15):
  index += 1
  weight_on_moon += weight_every_year
  print('Years', index, ', your weight is', round(weight_on_moon, 2), ' KG')
