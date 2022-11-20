#!/usr/bin/python

employees = { 'Alice': 100000, 'Bob': 99876, 'Carol': 100500, 'Frank': 88123, 'Eve': 93212 }

top_earners = []

for key, val in employees.items():
    if val >= 100000:
        top_earners.append((key, val))

print(top_earners)
# [('Alice', 100000), ('Carol', 100500)]


print([(k, v) for k, v in employees.items() if v >= 100000])
# [('Alice', 100000), ('Carol', 100500)]
