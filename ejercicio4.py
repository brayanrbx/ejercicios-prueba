dairy_products = ["Fairlife Milk", "Alta Dena Milk", "Queensland Butter"]
dairy_stock = [28, 36, 50]
cleaning_products = ["Windex", "Clorox Bleach", "Lysol Disinfectant Spray"]
cleaning_stock = [15, 20, 10]
grain_products = ["Rice", "Quinoa", "Oats"]
grain_stock = [40, 25, 30]

# Register a product
def setProduct(name, amount, group):
    global dairy_products, dairy_stock, cleaning_products, cleaning_stock, grain_products, grain_stock

    if group == "dairy":
        if name in dairy_products:
            position = dairy_products.index(name)
            dairy_stock[position] += amount
        else:
            dairy_products.append(name)
            dairy_stock.append(amount)
    elif group == "cleaning":
        if name in cleaning_products:
            position = cleaning_products.index(name)
            cleaning_stock[position] += amount
        else:
            cleaning_products.append(name)
            cleaning_stock.append(amount)
    elif group == "grain":
        if name in grain_products:
            position = grain_products.index(name)
            grain_stock[position] += amount
        else:
            grain_products.append(name)
            grain_stock.append(amount)
    else:
        print("group no valid")

# See all inventory
def seeInventory():
    print(f"""\tDairy inventory
          \r{'name'.ljust(30)} \tstock
          \r---------------------------------------------""")
    for i in range(len(dairy_products)):
        print(f"{dairy_products[i].ljust(30)} \t{dairy_stock[i]} in stock")
    print(f"""\n\tCleaning products inventory
          \r{'name'.ljust(30)} \tstock
          \r---------------------------------------------""")
    for i in range(len(cleaning_products)):
        print(f"{cleaning_products[i].ljust(30)} \t{cleaning_stock[i]} in stock")
    print(f"""\n\tGrain products inventory
          \r{'name'.ljust(30)} \tstock
          \r---------------------------------------------""")
    for i in range(len(grain_products)):
        print(f"{grain_products[i].ljust(30)} \t{grain_stock[i]} in stock")

# Set option

def setOption():
    print("""
          \r1. Agregar producto
          \r2. ver reporte de inventario
          \r3. salir
          """)
    op = int(input("Su opcion: "))
    if (op == 1):
        name = input("Ingrese el nombre del producto: ").capitalize()
        amount = int(input("Ingrese la cantidad: "))
        group = input("Ingrese si pertenece a dairy, cleaning o grain: ").lower()
        setProduct(name, amount, group)
        return True
    elif (op == 2):
        seeInventory()
    else:
        return False

condition = True

while(condition):
    print("""Bienvenido al sistema de Inventario.
          \rPor favor Ingrese una de las opciones:
          \r---------------------------------------------""")
    condition = setOption()
