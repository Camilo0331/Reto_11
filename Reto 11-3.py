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

