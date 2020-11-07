#!/usr/bin/python3
# Expected output:
# s
# e
# l
# a
# m
# a
# t
# d
# a
# t
# a
# n
# g

str = input("Input string: ")
s = 0
while len(str) > s:
  print(str[s::len(str)])
  s += 1
