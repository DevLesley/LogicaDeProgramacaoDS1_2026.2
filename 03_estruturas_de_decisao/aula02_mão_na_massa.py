## 🛠️ Prática do Aluno (Mão na Massa)
#Crie um programa que leia um número inteiro digitado pelo usuário e informe se o número é **PAR** ou **ÍMPAR**.
#*(Dica de Detetive: use o operador de módulo `% 2` para verificar o resto da divisão por 2!)*
import time
time.sleep(0.5)
print("Seja bem vindo ao verificador de números!!")
time.sleep(0.5)
print("")
numero = int(input("Digite um número: "))
if numero %2 == 0:
    print("Seu número é par.")
else:
    print("Seu número é ímpar.")