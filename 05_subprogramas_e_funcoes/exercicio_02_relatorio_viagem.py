"""
EXERCÍCIO 02: Modularizando Relatório de Viagem
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie duas funções:
1. `calcular_custo_transporte(distancia_km, consumo_kml, preco_combustivel)`
2. `calcular_custo_alimentacao(qtd_pessoas, dias, diaria_alimentacao)`

No programa principal, leia os dados, execute as funções e mostre o custo total da viagem.
"""

# TODO: Desenvolva as funções e o programa principal abaixo:
distancia_km = int(input("Digite a distância em km: "))
consumo_kml = int(input("Digite o consumo p/km: "))
preco_combustivel = int(input("Digite o preço do combustível: "))
qtd_pessoas = int(input("Digite a quantidade de pessoas: "))
dias = int(input("Digite quantos dias: "))
diaria_alimentacao = int(input("Digite a diária da alimentação: "))

def calcular_custo_transporte(distancia_km, consumo_kml, preco_combustivel) :
    valorTransporte = (distancia_km * consumo_kml) * preco_combustivel
    return calcular_custo_transporte
def calcular_custo_alimentacao(qtd_pessoas, dias, diaria_alimentacao) :
    valorAlimentacao = (qtd_pessoas * dias) * diaria_alimentacao
    return calcular_custo_alimentacao
valorTotal = (calcular_custo_alimentacao(qtd_pessoas, dias, diaria_alimentacao)) + (calcular_custo_transporte(distancia_km, consumo_kml, preco_combustivel))
print(f""" Com um custo de alimentação de: {calcular_custo_alimentacao(qtd_pessoas, dias, diaria_alimentacao)}
E um custo de transporte de: {calcular_custo_transporte(distancia_km, consumo_kml, preco_combustivel)}
O valor total ficou: {valorTotal}
""")
