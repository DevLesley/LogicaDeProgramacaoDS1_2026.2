"""
EXERCÍCIO 02: Aumento de Salário Escolar
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia o salário de um colaborador da escola e aplique o percentual de reajuste:
- 0.00 a 400.00: 15%
- 400.01 a 800.00: 12%
- 800.01 a 1200.00: 10%
- 1200.01 a 2000.00: 7%
- Acima de 2000.00: 4%

Imprima: novo salário, valor do reajuste ganho e percentual aplicado.
"""

# TODO: Desenvolva o algoritmo abaixo:

salario = float(input("Digite o seu salário recebido: "))
if salario >= 0.00 and salario <= 400.00:
    reajuste = salario * 0.15
    novo_salario = (reajuste + salario)
    print(f"Seu percentual de reajuste é de: 15% e seu reajuste é {reajuste}R$ e seu novo salário é {novo_salario}R$! Parabéns!!")
elif salario >= 400.01 and salario <= 800.00:
    reajuste = salario * 0.12
    novo_salario = (reajuste + salario)
    print(f"Seu percentual de reajuste é de: 12% e seu reajuste é {reajuste}R$ e seu novo salário é {novo_salario}R$! Parabéns!!")
elif salario >= 800.01 and salario <= 1200.00:
    reajuste = salario * 0.10
    novo_salario = (reajuste + salario)
    print(f"Seu percentual de reajuste é de: 10% e seu reajuste é {reajuste}R$ e seu novo salário é {novo_salario}R$! Parabéns!!")
elif salario >= 1200.01 and salario <= 2000.00:
    reajuste = salario * 0.07
    novo_salario = (reajuste + salario)
    print(f"Seu percentual de reajuste é de: 7% e seu reajuste é {reajuste}R$ e seu novo salário é {novo_salario}R$! Parabéns!!")
elif salario > 2000.00:
    reajuste = salario * 0.04
    novo_salario = (reajuste + salario)
    print(f"Seu percentual de reajuste é de: 4% e seu reajuste é {reajuste}R$ e seu novo salário é {novo_salario}R$! Parabéns!!")