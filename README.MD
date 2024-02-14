# Descripción de Ejercicios de Programación Básica

Este repositorio contiene soluciones a una serie de ejercicios de programación básica propuestos. Cada ejercicio tiene su propia solución en un archivo separado y este README proporciona una descripción de cada ejercicio junto con los pasos necesarios para compilar y ejecutar las soluciones.

## Ejercicio 1: Suma de serie repetida

Escriba una función que retorne la suma de una serie de X número repetido hasta el n-ésimo término.

- **Ejemplos:**
    Entrada : numero=3, terminos=5
    Salida : 37035 #(3 + 33 + 333 + 3333 + 33333)
    Entrada : numero=5, terminos=3
    Salida : 615 #(5 + 55 + 555)

## Ejercicio 2: Filtrado de números según condiciones

Escriba una función que retorne una lista de números que satisfagan ciertas condiciones.

1. El número debe ser divisible por cinco.
2. Si el número es mayor que 600, no se incluye en la salida.
3. Si el número es mayor que 1000, detenga el procesamiento y retorne el resultado.

- **Ejemplos:**
    Entrada : [24, 150, 300, 660, 295, 1050, 50]
    Salida : [150, 300, 295]
    Entrada : [110, 720, 307, 555, 1095, 12, 300, 1000]
    Salida : [110, 555]

## Ejercicio 3: Agrupación de elementos similares

Escriba una función para agrupar elementos similares en una lista de salida.

- **Ejemplos:**
    Entrada : [12, 25, 1, 1, 7, 25]
    Salida : \[[12], [7], [25, 25], [1, 1]]
    Entrada : [6, 7, 8, 9]
    Salida : \[[6], [7], [8], [9]]

## Ejercicio 4: Registro de inventario de productos

Desarrollar un programa de consola para organizar y registrar el inventario de productos en grupos.

1. Se requiere organizar el inventario en los siguientes grupos: dairy, cleaning y grain.
2. Cada grupo tiene que estar asociado a un elemento de otra lista que almacena las existencias de ese grupo en la misma posición, como en el siguiente ejemplo:
dairy_products = [“Fairlife Milk”, “Alta Dena Milk”, “Queensland Butter”]
dairy_stock = [28, 36, 50]
En donde, por ejemplo, el producto del grupo dairy “Alta Dena Milk” tiene una existencia de 36 unidades.
3. Para un producto entrante, se debe poder registrar en el sistema: el nombre del producto, la cantidad y el grupo
al que pertenece.Globaltek Development S.A - Programación Básica -Juan C. Hernández, Oct 2022
4. Si el producto no existe en la lista, se debe agregar al final con su cantidad entrante, pero si existe se debe
actualizar el número de existencias sumando la nueva cantidad.
5. El programa debe permitir visualizar todo el inventario de productos y existencias.

## Requerimientos
- Python 3.x

## Pasos para compilar y ejecutar
1. Clone o descargue los archivos de este repositorio en su máquina local.
2. Abra un terminal o línea de comandos y navegue al directorio donde se encuentran los archivos.
3. Para ejecutar cada ejercicio, simplemente ejecute el archivo Python correspondiente.