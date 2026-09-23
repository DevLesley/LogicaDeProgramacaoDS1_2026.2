"""
EXERCÍCIO 04: Cardápio da Lanchonete
Disciplina: Lógica de Programação com Python

TABELA:
1 - Cachorro Quente: R$ 4.00
2 - X-Salada: R$ 4.50
3 - X-Bacon: R$ 5.00
4 - Torrada Simples: R$ 2.00
5 - Refrigerante: R$ 1.50

ENUNCIADO:
Leia o código do item e a quantidade consumida.
Calcule e mostre o total a pagar.
"""

# TODO: Desenvolva o algoritmo abaixo:
import time
print("1 - Cachorro Quente: R$ 4.00")
time.sleep(0.25)
print("2 - X-Salada: R$ 4.50")
time.sleep(0.25)
print("3 - X-Bacon: R$ 5.00")
time.sleep(0.25)
print("4 - Torrada Simples: R$ 2.00")
time.sleep(0.25)
print("5 - Refrigerante: R$ 1.50")
time.sleep(1)
opção = int(input("Digite o numero do item você quer pedir: "))
match opção:
    case 1:
        numero = int(input("Digite a quantidade que você quer pedir: "))
        valor = numero * 4.00
        print(f"O total do pedido ficou: {valor}R$, você pediu {numero}: ")
    case 2:
        numero = int(input("Digite a quantidade que você quer pedir: "))
        valor = numero * 4.50
        print(f"O total do pedido ficou: {valor}R$, você pediu {numero}: ")
    case 3:
        numero = int(input("Digite a quantidade que você quer pedir: "))
        valor = numero * 5.00
        print(f"O total do pedido ficou: {valor}R$, você pediu {numero}: ")
    case 4:
        numero = int(input("Digite a quantidade que você quer pedir: "))
        valor = numero * 2.00
        print(f"O total do pedido ficou: {valor}R$, você pediu {numero}: ")
    case 5:
        numero = int(input("Digite a quantidade que você quer pedir: "))
        valor = numero * 1.50
        print(f"O total do pedido ficou: {valor}R$, você pediu {numero}: ")
    case _:
        print("Você não escolheu um número valido, tente novamente.")