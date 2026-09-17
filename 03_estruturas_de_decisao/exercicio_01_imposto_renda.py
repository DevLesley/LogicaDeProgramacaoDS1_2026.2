"""
EXERCÍCIO 01: Imposto de Renda de Lisarb
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia o salário de uma pessoa em Rombus (R$).
- Até R$ 2000.00: Isento
- De R$ 2000.01 até R$ 3000.00: 8% sobre o excedente de R$ 2000.00
- De R$ 3000.01 até R$ 4500.00: 18% sobre o excedente de R$ 3000.00 + 8% da faixa anterior
- Acima de R$ 4500.00: 28% sobre o que ultrapassar R$ 4500.00 + impostos anteriores

Imprima "Isento" ou o valor total do imposto formatado com 2 casas decimais.
"""

# TODO: Desenvolva o algoritmo abaixo:

print("Seja bem vindo ao calculador de imposto de renda!!")
print(" ")
nome = input("Digite seu nome de usuário: ")
salario = float(input("Digite seu salário: "))
print(" ")


if (salario <= 2000.00):
    print(f"Parabéns {nome} você está isendo de impostos")
elif (salario <= 3000.00 and salario > 2000):
    taxa1 = (salario) * 0.08
    valor = (taxa1) + salario
    print(f"Você deve pagar um total de: {valor}R$ e {taxa1}R$ de imposto")
    
elif (salario <= 4500.00 and salario > 3000):
    taxa1 = (1000) * 0.08
    taxa2 = ((salario - 3000) * 0.18) + taxa1
    valor = (taxa2) + salario
    print(f"Você deve pagar um total de: {valor}R$ e {taxa2}R$ de imposto")
elif (salario > 4500):
    taxa1 = (1000) * 0.08
    taxa2 = ((3000) * 0.18) + taxa1
    taxa3 = ((salario - 4500) * 0.28) + taxa2
    valor = (taxa3) + salario
    print(f"Você deve pagar um total de: {valor}R$ e {taxa3}R$ de imposto")

