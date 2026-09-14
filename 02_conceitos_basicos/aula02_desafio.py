## 🛠️ Prática do Aluno (Mão na Massa)
#Escreva um programa que solicite ao usuário:
#1. O valor de uma conta de restaurante.
#2. A quantidade de amigos presentes na mesa para dividir a conta igualmente.

#O programa deve calcular e exibir quanto cada amigo deve pagar, formatando o valor com duas casas decimais.


valor_conta = float(input("Digite o valor da conta do restaurante: "))
amigos = int(input("Digite a quantidade de amigos: "))

valor_final = ((valor_conta) / (amigos))
print(f"O valor que cada um deve pagar é: {valor_final:.2f}")