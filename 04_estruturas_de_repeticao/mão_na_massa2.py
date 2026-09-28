# 🛠️ Prática do Aluno (Mão na Massa)
#Escreva um programa com laço `while` que leia números inteiros digitados pelo usuário até que ele digite o número `0` (flag de parada). Ao final, o programa deve exibir a soma de todos os números digitados.
soma = 0
numero = int(input("Digite um numero inteiro: "))
while numero != 0:
    soma = soma + numero
    print("Condição falsa, digite outro numero inteiro.")
    numero = int(input("Digite um numero inteiro: "))
print(f"no total ficou {soma} para que a soma fosse verdadeira")