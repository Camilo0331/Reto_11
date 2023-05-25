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
    