import random

length = int(input("Enter lenght of the set: "))
arr = []

for i in range(length):
    arr.append(random.randint(-length, length))

try:
    aleatory = open(f'{length}aleatory.txt', 'w')

    for i in range(length):
        aleatory.write(f"{arr[i]}\n")
except:
    print("Aleatory file fail.")
else:
    aleatory.close()

arr.sort()

try:
    ascending = open(f'{length}ascending.txt', 'w')

    for i in range(length):
        ascending.write(f"{arr[i]}\n")
except:
    print("Ascending file fail.")
else:
    ascending.close()

arr.reverse()

try:
    descending = open(f'{length}descending.txt', 'w')

    for i in range(length):
        descending.write(f"{arr[i]}\n")
except:
    print("Descending file fail.")
else:
    descending.close()
