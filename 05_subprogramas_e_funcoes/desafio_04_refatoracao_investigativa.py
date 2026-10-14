"""
DESAFIO 04: REFATORAÇÃO INVESTIGATIVA
Disciplina: Lógica de Programação com Python

RELATÓRIO DA INVESTIGAÇÃO:
O código monolítico repete cálculos de desconto e impostos várias vezes.

SUA MISSÃO:
1. Crie uma função calcular_preco_final(preco_base, taxa_desc, taxa_imp) com return.
2. Crie um procedimento exibir_relatorio_item(numero_item, preco_final) com print.
3. Teste suas funções refatoradas.
"""

# TODO: Desenvolva as funções modulares abaixo:

numero_item = int(input("Digite o número do item: "))
preco_base = int(input("Digite o preço base: "))
taxa_desc = int(input("Digite a taxa de desconto: "))
taxa_imp = int(input("Digite a taxa de imposto: "))
def calcular_preco_final(preco_base, taxa_desc, taxa_imp) :
    desconto = preco_base * taxa_desc
    imposto = preco_base * taxa_imp
    preco_final = (preco_base + taxa_imp) - taxa_desc
    print(f"O número do item escolhido é: {numero_item}, e o preço final é {preco_final}.")
    return
calcular_preco_final(preco_base, taxa_desc, taxa_imp)