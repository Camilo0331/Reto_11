# Reto_11

## Punto 1

Desarrolle un programa que permita realizar la suma/resta de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.

```
def sumar(lista1:list,lista2:list):
    lista9=[]
    for i in range(len(lista1)):
        lista4 = []
        for n in range(len(lista1[i])):
            suma = (lista1[i][n])+(lista2[i][n])
            lista4.append(suma)
        lista9.append(lista4)
    return lista9


def encontrar(a:int, b:int):
    lista5 =[]
    for i in range(a):
        lista4=[]
        for n in range(b):
            p = int(input("Ingrese el numero que va en las corrdenadas "+str(i+1)+" , "+str(n+1)+" : "))
            lista4.append(p)
        lista5.append(lista4)
    return lista5

if __name__=="__main__":
    a = int(input("Ingrese la cantidad de filas de las matrices: "))
    b = int(input("Ingrese la cantidad de columnas de las matrices: "))
    lista5 = encontrar(a,b)
    lista6 = encontrar(a,b)
    print(lista5)
    print(lista6)
    suma = sumar(lista5,lista6)
    print(suma)
```
## Punto 2

Desarrolle un programa que permita realizar el producto de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.

```
def crearMatriz1(a: int, b:int):
    lista1 = []
    for i in range(a):
        lista2 = []
        for n in range(b):
            u = int(input("Ingrese el número en el espacio "+str(i+1)+" , "+str(n+1)+" : "))
            lista2.append(u)
        lista1.append(lista2)
    return lista1

def crearMatriz2(a: int, b:int):
    lista1 = []
    for i in range(b):
        lista2 = []
        for n in range(a):
            u = int(input("Ingrese los número para la segunda matriz en el espacio "+str(i+1)+" , "+str(n+1)+" : "))
            lista2.append(u)
        lista1.append(lista2)
    return lista1


if __name__=="__main__":
    a = int(input("Ingrese la cantidad de filas: "))
    b = int(input("Ingrese la cantidad de columnas: "))
    matriz1 = crearMatriz1(a,b)
    matriz2 = crearMatriz2(a,b)
    for i in range(len(matriz1)):
        print(str(matriz1[i]))
    for i in range(len(matriz2)):
        print(str(matriz2[i]))
```

## Punto 3

Desarrolle un programa que permita obtener la matriz transpuesta de una matriz ingresada. El programa debe validar las condiciones necesarias para ejecutar la operación.

```
def crearMatriz(a:int,b:int):
    lista1 =[]
    for i in range(a):
        lista2 = []
        for n in range(b):
            p = int(input("Ingrese el número en la posición "+str(i+1)+" , "+str(n+1)+" : "))
            lista2.append(p)
        lista1.append(lista2)
    return lista1

def transpuesta(lista3:list, a: int, b:int):
    lista4 = []
    for i in range(b):
        lista5 = []
        for n in range(a):
            u = lista3[n][i]
            lista5.append(u)
        lista4.append(lista5)
    return lista4

def imprimir(lista6:list):
    for i in range(len(lista6)):
        print(lista6[i])
    return
    


if __name__=="__main__":
    a = int(input("Ingrese el número de filas de la matriz: "))
    b = int(input("Ingrese el número de columnas que quiere: "))

    matriz = crearMatriz(a,b)
    imp = imprimir(matriz)
    print(str(imp))


    print("La matriz ingresada transpuesta es")
    
    matrizTranspuesta = transpuesta(matriz,a,b)
    imp2 = imprimir(matrizTranspuesta)
    print(str(imp2))
```

## Punto 4

Desarrollar un programa que sume los elementos de una columna dada de una matriz.

```
def crearMatriz(a:int,b:int):
    lista1 =[]
    for i in range(a):
        lista2 = []
        for n in range(b):
            p = int(input("Ingrese el número en la posición "+str(i+1)+" , "+str(n+1)+" : "))
            lista2.append(p)
        lista1.append(lista2)
    return lista1

def sumarColumnas(lista1:list,a:int,b:int):
    lista2 = []
    for i in range(b):
        u = 0
        for n in range(a):
            u += lista1[n][i]
        lista2.append(u)
    return lista2

if __name__=="__main__":
    a = int(input("Ingrese el número de filas de la matriz: "))
    b = int(input("Ingrese el número de columnas que quiere: "))
    matriz = crearMatriz(a,b)
    for i in matriz:
        print(i)
    print("La suma de sus columnas")
    matriz2 = sumarColumnas(matriz,a,b)
    print(matriz2)

```

## Punto 5

Desarrollar un programa que sume los elementos de una fila dada de una matriz.


```
def crearMatriz(a:int,b:int):
    lista1 =[]
    for i in range(a):
        lista2 = []
        for n in range(b):
            p = int(input("Ingrese el número en la posición "+str(i+1)+" , "+str(n+1)+" : "))
            lista2.append(p)
        lista1.append(lista2)
    return lista1

def sumarColumnas(lista1:list,a:int,b:int):
    lista2 = []
    for i in range(a):
        u = 0
        for n in range(b):
            u += lista1[i][n]
        lista2.append(u)
    return lista2

if __name__=="__main__":
    a = int(input("Ingrese el número de filas de la matriz: "))
    b = int(input("Ingrese el número de columnas que quiere: "))
    matriz = crearMatriz(a,b)
    for i in matriz:
        print(i)
    print("La suma de sus filas")
    matriz2 = sumarColumnas(matriz,a,b)
    for i in matriz2:
        print(i)
    
```

### ¡Gracias por ver el repo!
