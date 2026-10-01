"""
EXERCÍCIO 04: Positivos e Média
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia 6 valores numéricos.
Conte quantos foram estritamente positivos (> 0) e calcule a média aritmética deles.
Imprima a quantidade de positivos e a média formatada com 1 casa decimal.
"""

# TODO: Desenvolva o algoritmo abaixo:
contador_positivo = 0
for numero in range(6):
    if numero > 0:
        contador_positivo = contador_positivo + 1
    elif numero > 0:
        