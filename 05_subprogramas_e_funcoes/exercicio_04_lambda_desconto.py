"""
EXERCÍCIO 04: Função Lambda de Desconto Casas Paulino
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Escreva uma função anônima (lambda) que receba o valor de um produto
e retorne o valor com 15% de desconto à vista aplicado.
"""

# TODO: Desenvolva a expressão lambda e teste-a abaixo:

valor1 = float(input("Digite o valor a seguir: "))
calcular_acrescimo = lambda acrescimo: (valor1 * 0.15) + valor1
print(f"""Seu valor sem o acréscimo é: {valor1}.
Com o acréscimo é: {calcular_acrescimo(valor1)}.
""")