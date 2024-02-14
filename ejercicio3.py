def group(arr):
    arrOut = {}
    for i in arr:
        if i in arrOut:
            arrOut[i].append(i)
        else:
            arrOut[i] = [i]
    return list(arrOut.values())

# arr1 = [12, 25, 1, 1, 7, 25]
# arr2 = [6, 7, 8, 9]

# print(group(arr1))
# print(group(arr2))

arr_input = input("Ingrese los elementos de la lista separados por comas: ")

arr = [int(x) for x in arr_input.split(',')]

print(group(arr))