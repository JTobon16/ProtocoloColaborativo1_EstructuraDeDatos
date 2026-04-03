
#cree la matriz 3x3 de acuerdo a los parametros
def crear_matriz_3x3():
    """
    Crea una matriz 3x3 con valores del 1 al 9
    Representacion: lista de listas
    """
    return [[1 + j + 3 * i for j in range(3)] for i in range(3)]


def imprimir_matriz(matriz):
    """
    matriz en forma de tabla
    """
    print("Matriz:")
    for fila in matriz:
        for valor in fila:
            print(f"{valor:3}", end=" ")
        print()
    print()

#recorrer las columnas por columnas
def recorrer_por_columnas(matriz):
    """
    Recorre la matriz por columnas
    """
    print("Recorrido por columnas:")
    filas = len(matriz)
    columnas = len(matriz[0])
    for col in range(columnas):
        for fila in range(filas):
            print(f"{matriz[fila][col]:3}", end=" ")
        print()
    print()

#sumar los elementos aleatorios de la matriz
def sumar_elementos(matriz):
    """
    Suma todos los elementos de la matriz
    """
    total = 0
    for fila in matriz:
        total += sum(fila)
    return total

#el intercambio de filas
def intercambiar_filas(matriz):
    """
    Intercambia la primera fila con la última
    """
    matriz[0], matriz[-1] = matriz[-1], matriz[0]
    return matriz


# ejecucion del programa
if __name__ == "__main__":
    mat = crear_matriz_3x3()

    # Imprimir matriz original
    imprimir_matriz(mat)

    # Recorrer por columnas
    recorrer_por_columnas(mat)

    # Sumar todos los elementos
    suma = sumar_elementos(mat)
    print(f"Suma de todos los elementos: {suma}\n")

    # Intercambiar primera y última fila
    mat = intercambiar_filas(mat)
    print("Matriz después de intercambiar primera y última fila:")
    imprimir_matriz(mat)