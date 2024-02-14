def listOut(arr):
    arrOut = []
    for i in arr:
        if ((i % 5 == 0) and i <= 600):
            arrOut.append(i)
        if (i > 1000):
            break
    return arrOut

# arr1 = [24, 150, 300, 660, 295, 1050, 50]
# arr2 = [110, 720, 307, 555, 1095, 12, 300, 1000]

# print(listOut(arr1))
# print(listOut(arr2))

arr_input = input("Ingrese los elementos de la lista separados por comas: ")

arr = [int(x) for x in arr_input.split(',')]

print(listOut(arr))