
import random

def crear_arreglo(n):
    """Crea un arreglo de n enteros aleatorios entre 1 y 100"""
    return [random.randint(1, 100) for _ in range(n)]

def recorrer_for_clasico(arr):
    print("Recorrido FOR clasico:")
    for i in range(len(arr)):
        print(f"Indice {i}: {arr[i]}")

def recorrer_for_each(arr):
    print("Recorrido FOR-EACH:")
    for valor in arr:
        print(valor)

#modificacion
def modificar_arreglo(arr):
    """Cambiar impares por 0 y multiplicar por indice"""
    for i in range(len(arr)):
        if arr[i] % 2 != 0:
            arr[i] = 0
        arr[i] *= i
    return arr

#busqueda
def busqueda_lineal(arr, valor):
    """Retorna indice si se encuentra, -1 si no"""
    for i, v in enumerate(arr):
        if v == valor:
            return i
    return -1

# Prueba del arreglo (este es el main en python)
if __name__ == "__main__":
    arr = crear_arreglo(10)
    recorrer_for_clasico(arr)
    recorrer_for_each(arr)
    print("Modificado:", modificar_arreglo(arr))
    print("Búsqueda 50:", busqueda_lineal(arr, 50))