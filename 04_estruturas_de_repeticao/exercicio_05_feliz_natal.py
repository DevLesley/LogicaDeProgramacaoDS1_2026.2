"""
EXERCÍCIO 05: Feliz Nataaal!
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Receba um número inteiro I (nível de empolgação).
Utilize repetição para exibir a frase "Feliz natal!" repetindo a letra 'a'
da palavra natal exatamente I vezes (ex: I=5 -> "Feliz nataaaal!").
"""

# TODO: Desenvolva o algoritmo abaixo:

nivel_empolgacao = int(input("Digite seu nivel de empolgação: "))
numero = -2
a = "a"
for i in range(nivel_empolgacao):
    numero = numero + 1
print(f"Feliz nata{numero * a}l!")