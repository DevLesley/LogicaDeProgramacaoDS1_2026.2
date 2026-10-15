## 🛠️ Prática do Aluno (Mão na Massa)
#Escreva uma função `lambda` chamada `calcular_acrescimo` que receba um valor numérico e retorne esse valor com 10% de acréscimo.

valor1 = float(input("Digite o valor a seguir: "))
calcular_acrescimo = lambda acrescimo: (valor1 * 0.1) + valor1
print(f"""Seu valor sem o acréscimo é: {valor1}!!
Com o acréscimo é: {calcular_acrescimo(valor1)}!!
""")