import time


# BUSQUEDA LINEAL

def busqueda_lineal(lista, objetivo):
    for indice, elemento in enumerate(lista):
        if elemento == objetivo:
            return indice
    return -1



# BUSQUEDA BINARIA

def busqueda_binaria(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1

    return -1


# PRUEBAS

# Pruebas para la búsqueda lineal
lista1 = [1, 2, 3, 4, 5]
objetivo1 = 3
print(busqueda_lineal(lista1, objetivo1))  # Deberia devolver 2

objetivo2 = 6
print(busqueda_lineal(lista1, objetivo2))  # Deberia devolver -1

# Pruebas para la búsqueda binaria
lista2 = [10, 20, 30, 40, 50]
objetivo3 = 30
print(busqueda_binaria(lista2, objetivo3))  # Deberia devolver 2

objetivo4 = 60
print(busqueda_binaria(lista2, objetivo4))  # Deberia devolver -1


# EFICIENCIA

def medir_tiempo(funcion, *args):
    inicio = time.time()
    resultado = funcion(*args)
    fin = time.time()
    return resultado, fin - inicio


lista_grande = list(range(1000000))
objetivo_presente = 999999
objetivo_ausente = 1000000

# Medición para búsqueda lineal
resultado, tiempo = medir_tiempo(busqueda_lineal, lista_grande, objetivo_presente)
print(f"Lineal - Objetivo presente: Resultado {resultado}, Tiempo {tiempo} segundos")

resultado, tiempo = medir_tiempo(busqueda_lineal, lista_grande, objetivo_ausente)
print(f"Lineal - Objetivo ausente: Resultado {resultado}, Tiempo {tiempo} segundos")


# Medición para búsqueda binaria
resultado, tiempo = medir_tiempo(busqueda_binaria, lista_grande, objetivo_presente)
print(f"Binaria - Objetivo presente: Resultado {resultado}, Tiempo {tiempo} segundos")

resultado, tiempo = medir_tiempo(busqueda_binaria, lista_grande, objetivo_ausente)
print(f"Binaria - Objetivo ausente: Resultado {resultado}, Tiempo {tiempo} segundos")


