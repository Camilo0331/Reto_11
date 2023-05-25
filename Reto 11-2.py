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
