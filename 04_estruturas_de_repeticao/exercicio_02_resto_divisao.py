"""
EXERCÍCIO 02: Resto da Divisão por 5
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia dois valores inteiros X e Y.
Utilize o laço for para imprimir todos os inteiros entre X e Y (em ordem crescente)
cujo resto da divisão por 5 seja igual a 2 ou igual a 3.
"""

# TODO: Desenvolva o algoritmo abaixo:

valor1 = int(input("Digite o valor 1: "))
valor2 = int(input("Digite o valor 2: "))
minimo = min(valor1, valor2)
maximo = max(valor1, valor2)
for i in range (minimo + 1, maximo):
    i2 = i % 5
    if (i2 == 2) or (i2 == 3):
        print(f"A divisão do numero: {i} é igual a 2 ou 3")
