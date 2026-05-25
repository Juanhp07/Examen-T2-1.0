import random


def buscar_max_min(lista, indice, maximo, minimo):
    if indice == len(lista):
        return maximo, minimo

    elemento = lista[indice]

    if elemento % 3 == 0:
        if maximo is None:
            maximo = elemento
            minimo = elemento
        else:
            if elemento > maximo:
                maximo = elemento
            if elemento < minimo:
                minimo = elemento

    return buscar_max_min(lista, indice + 1, maximo, minimo)


def calcular_promedio(lista):
    maximo, minimo = buscar_max_min(lista, 0, None, None)
    if maximo is None:
        return None, None, None
    return maximo, minimo, (maximo + minimo) / 2


def generar_numero_aleatorio():
    cifras = random.randint(2, 4)
    minimo = 10 ** (cifras - 1)
    maximo = (10 ** cifras) - 1
    return random.randint(minimo, maximo)


def obtener_tamano():
    while True:
        try:
            n = int(input("Ingresa el tamaño del arreglo: "))
            if n > 0:
                return n
            print("Error: el tamaño debe ser mayor a 0.")
        except ValueError:
            print("Error: ingresa un número entero válido.")


def mostrar_resultado(arreglo, maximo, minimo, promedio):
    multiplos = [x for x in arreglo if x % 3 == 0]
    print("\n" + "-" * 50)
    print(f"Arreglo generado     : {arreglo}")
    print(f"Múltiplos de 3       : {multiplos}")
    print(f"Máximo               : {maximo}")
    print(f"Mínimo               : {minimo}")
    print(f"Promedio (max+min)/2 : ({maximo}+{minimo})/2 = {promedio}")
    print("-" * 50)


def main():
    print("=" * 50)
    print("   PROMEDIO ENTRE MAX Y MIN - MÚLTIPLOS DE 3")
    print("=" * 50 + "\n")

    n = obtener_tamano()
    arreglo = [generar_numero_aleatorio() for _ in range(n)]
    maximo, minimo, promedio = calcular_promedio(arreglo)

    if promedio is None:
        print(f"\nArreglo generado: {arreglo}")
        print("No se encontraron múltiplos de 3 en el arreglo.")
    else:
        mostrar_resultado(arreglo, maximo, minimo, promedio)


if __name__ == "__main__":
    main()