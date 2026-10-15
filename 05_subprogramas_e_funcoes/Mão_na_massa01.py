## 🛠️ Prática do Aluno (Mão na Massa)
#Crie uma função chamada `calcular_media(nota1, nota2, nota3)` que receba três notas e retorne a média aritmética simples dessas notas.

# TODO: Defina a função calcular_media e teste-a abaixo
nota1 = int(input("Digite a nota 1: "))
nota2 = int(input("Digite a nota 2: "))
nota3 = int(input("Digite a nota 3: "))
def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    print(f"Sua média aritmética simples é: {media}.")
calcular_media(nota1, nota2, nota3)

