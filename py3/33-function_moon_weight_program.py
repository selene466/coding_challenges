#!/usr/bin/env python3
'''
Moon Weight Program
Soal:
Instead of a simple function, where you pass in the values as parameters, you can make a mini-program that prompts for the values using sys.stdin.readline(). In this case, you call the function whitout any parameters at all:

>>> moon_weight()

Recyling Your Code with Functions and Modules. The function will display a message asking for the starting weight, then a second message asking for the amount the weight will increase each year, and finally a message asking for the number of years. You would see something like the following:

Please enter your current Earth weight
45

Please enter the amount your weight might increase each year
0.4

Please enter the number of years
12

Remember to import the sys module first before creating your function:
>>> import sys
'''

import sys

def moon_weight():
  print('Please enter your current Earth weight')
  current_earth_weight = sys.stdin.readline()
  try:
    current_earth_weight = float(current_earth_weight)
  except ValueError:
    exit('Invalid input')
  print()
  print('Please enter the amount your weight might increase each year')
  might_increased_weight = sys.stdin.readline()
  try:
    might_increased_weight = float(might_increased_weight)
  except ValueError:
    exit('Invalid input')
  print()
  print('Please enter the number of years')
  years_on_moon = sys.stdin.readline()
  try:
    years_on_moon = int(years_on_moon)
  except ValueError:
    exit('Invalid input')

  for y in range(years_on_moon):
    current_earth_weight += might_increased_weight

  weight_on_moon = current_earth_weight * 0.165

  print()
  print('In', years_on_moon, 'years, Your estimated final moon weight:', round(weight_on_moon, 2))

moon_weight()
