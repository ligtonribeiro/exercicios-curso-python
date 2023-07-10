contador = 0
notas = []

def calcula_media_aritmetica(notas: list) -> float:
    soma = 0
    for nota in notas:
        soma = nota + soma
    return soma / len(notas)

total_notas = int(input("Total de notas para calcular a média: "))

while contador < total_notas:
    nota = float(input("Digite a nota: "))
    notas.append(nota)
    contador += 1

print("A média das notas é: {:.2f}".format(calcula_media_aritmetica(notas)))