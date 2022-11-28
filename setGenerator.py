import random

def saveFiles(floor: int, ceiling: int, length: int, saveAleatory: bool, saveAscending: bool, saveDescending: bool, location: str):
    arr = []
    arrSorted = False

    for i in range(length):
        arr.append(random.randint(floor, ceiling))

    if saveAleatory:
        try:
            aleatory = open(f'{location}aleatory.txt', 'w')

            for i in range(length):
                aleatory.write(f"{arr[i]}\n")
        except:
            print("Aleatory file fail.")
        else:
            aleatory.close()

    if saveAscending:
        arr.sort()
        arrSorted = True

        try:
            ascending = open(f'{location}ascending.txt', 'w')

            for i in range(length):
                ascending.write(f"{arr[i]}\n")
        except:
            print("Ascending file fail.")
        else:
            ascending.close()

    if saveDescending:
        if arrSorted:
            arr.reverse()
        else:
            arr.sort()
            arr.reverse()

        try:
            descending = open(f'{location}descending.txt', 'w')

            for i in range(length):
                descending.write(f"{arr[i]}\n")
        except:
            print("Descending file fail.")
        else:
            descending.close()
