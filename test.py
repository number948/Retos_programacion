myArray = [22, 5, 3, 6, 1]
mayor = myArray[0]

for i in range(1, len(myArray)):
    if myArray[i] > mayor:
        mayor = myArray[i]
print(mayor)


