"""
EXERCÍCIO 03: Fórmula de Bhaskara
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia 3 valores de ponto flutuante (A, B e C) de uma equação do 2º grau.
- Se A for 0 ou delta for negativo, imprima "Impossivel calcular".
- Caso contrário, calcule e mostre as duas raízes (R1 e R2) formatadas com 5 casas decimais.
"""

# TODO: Desenvolva o algoritmo abaixo:
import math
a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))
delta = b**2 - 4*a*c
if a == 0 or delta < 0:
    print("Impossível calcular...")
else:
    raiz1 = (-b + math.sqrt(delta)) / (2*a)
    raiz2 = (-b - math.sqrt(delta)) / (2*a)
    print(f"A sua primeira raiz é: {raiz1:.5f}. E a sua segunda raiz é: {raiz2:.5f}.")