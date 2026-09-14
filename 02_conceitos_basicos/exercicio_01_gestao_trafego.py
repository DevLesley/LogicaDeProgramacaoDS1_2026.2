"""
EXERCÍCIO 01: Gestão de Tráfego Casas Paulino
Disciplina: Lógica de Programação com Python

ENUNCIADO:
A loja Casas Paulino está veiculando anúncios no Meta Ads em Tianguá.
Escreva um programa que leia:
1. O valor total investido na campanha (em R$).
2. O número total de cliques obtidos.

Calcule e mostre na tela o Custo Por Clique (CPC) médio da campanha formatado em reais.
"""

# TODO: Desenvolva o algoritmo abaixo:

valor_investido_campanha = float(input("Digite o valor investido na campanha: "))
total_cliques = int(input("Digite o total de cliques: "))
custo_clique = (valor_investido_campanha/total_cliques)
print(f"O custo por clique é: R${custo_clique:.2f}")