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