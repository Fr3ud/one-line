#!/usr/bin/python

squares = []

for i in range(10):
    squares.append(i**2)

print(squares)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


print([i ** 2 for i in range(10)])
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
