"""
EXERCÍCIO 02: Consumo da Kawasaki Versys 300
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Para planejar uma viagem técnica de Tianguá até o Beach Park (Aquiraz),
solicite:
1. A distância total percorrida (em Km).
2. O total de combustível gasto (em Litros).

Calcule e imprima o consumo médio da motocicleta (Km/L) formatado com 2 casas decimais.
"""

# TODO: Desenvolva o algoritmo abaixo:

distancia_percorrida = float(input("Digite a distância percorrida: "))
litros_gasto = float(input("Digite quantos litros de combustivel foram gastos: "))

valor = (distancia_percorrida/litros_gasto)
print(f"O consumo médio da motocicleta é {valor:.2f}(Km/L)")