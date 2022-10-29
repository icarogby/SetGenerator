import random

length = 5
arr = []

for i in range(length):
    arr.append(random.randint(-length, length))

try:
    aleatory = open(f'{length}aleatory.txt', 'w')

    for i in range(length):
        aleatory.write(f"{arr[i]}\n")
finally:
    aleatory.close()

print(arr)

"""
arr.sort()

print(arr)

arr.reverse()

print(arr)
"""
