def repeatedSum(num, repeated):
    result = 0
    num_str = str(num)
    i = 1;
    while (i <= repeated):
        term = int(num_str * i)
        result += term
        i += 1
    return result

# print(repeatedSum(3,5))
# print(repeatedSum(5,3))

num = int(input("Ingrese el número: "))
repeated = int(input("Ingrese el número de veces a repetirlo: "))

print(repeatedSum(num, repeated))


