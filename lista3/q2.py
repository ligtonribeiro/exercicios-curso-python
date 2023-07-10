numeros = [70, 3, 1, 5, 30, 20, 31, 40, 60, 51]

def retorna_pares(lista_numeros: list) -> list:
    pares = []
    for num in lista_numeros:
        if num % 2 == 0:
            pares.append(num)
    return pares

def retorna_impares(lista_numeros: list) -> list:
    impares = []
    for num in lista_numeros:
        if num % 2 != 0:
            impares.append(num)
    return impares

def ordena_lista(lista_numeros: list) -> list:
    return sorted(lista_numeros)

print(f"Valores pares: {retorna_pares(numeros)}")
print(f"Valores impares: {retorna_impares(numeros)}")
print(f"Valores impares: {ordena_lista(numeros)}")