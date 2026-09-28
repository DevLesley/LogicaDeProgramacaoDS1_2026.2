## 🛠️ Prática do Aluno (Mão na Massa)
#Crie um programa que solicite um número inteiro ao usuário e imprima a **tabuada de multiplicação**
#  desse número de 1 até 10 usando o laço `for`.
import time
numero = int(input("Digite um número inteiro para ver sua tabuada: "))
for i in range(1, 11):
    print(f"{numero} X {i}:")
    print(i * numero)
    time.sleep(0.5)