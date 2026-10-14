"""
EXERCÍCIO 01: Pontuação OBI (Astro Lume Devs)
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie uma função nomeada `calcular_pontuacao_total(fase1, fase2, fase3)` com a diretiva `def`
que receba as 3 notas como parâmetros e retorne a pontuação total da equipe.
"""

# TODO: Desenvolva a função e os testes abaixo:
fase1 = int(input("Digite um valor: "))
fase2 = int(input("Digite um valor: "))
fase3 = int(input("Digite um valor: "))
def calcular_pontuacao_total(fase1, fase2, fase3) :
    valor = fase1 + fase2 + fase3
    print(f"A pontuação total da equipe é: {valor} Pontos!")
calcular_pontuacao_total(fase1, fase2, fase3)