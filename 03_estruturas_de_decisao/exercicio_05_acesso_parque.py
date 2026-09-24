"""
EXERCÍCIO 05: Acesso à Bilheteria do Parque
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Receba a idade do visitante (valor base do ingresso: R$ 100,00):
- Menor que 12 anos: "Infantil" (50% de desconto -> R$ 50,00)
- Maior ou igual a 60 anos: "Melhor Idade" (Gratuidade -> R$ 0,00)
- Demais idades: "Integral" (R$ 100,00)

Imprima o tipo de bilhete e o valor final a pagar.
"""

# TODO: Desenvolva o algoritmo abaixo:


nome = input("Digite o seu nome: ")
idade = int(input("Digite sua idade(ex:16 anos): "))
if idade < 12:
    desconto = 0.5 
    preco = 100 * desconto
    print(f"{nome} seu bilhete custará {preco}R$ você recebeu 50% de desconto!!")
elif idade >= 60:
    desconto = 0.0 
    preco = 100 * desconto
    print(f"{nome} seu bilhete custará {preco}R$ com 100% de desconto!!")
elif idade >= 12 <60:
    desconto = 1 
    preco = 100 * desconto
    print(f"{nome} seu bilhete custará {preco}R$ pagando o valor integral!!")