"""
EXERCÍCIO 04: Positivos e Média
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia 6 valores numéricos.
Conte quantos foram estritamente positivos (> 0) e calcule a média aritmética deles.
Imprima a quantidade de positivos e a média formatada com 1 casa decimal.
"""

# TODO: Desenvolva o algoritmo abaixo:
lista_valores = []
contador_positivo = 0
valor = 0
while valor != 6:
    numero = int(input("Digite o seu número: "))
    valor = valor + 1
    if valor == 6:
        media = sum(lista_valores) / len(lista_valores)
    if numero > 0:
        contador_positivo = contador_positivo + 1
    if numero > 0:
        lista_valores.append(numero)
    else:
        ("")
print(f"Você digitou {contador_positivo} números positivos e a média dos numeros positivos é {media:.2f}!!")