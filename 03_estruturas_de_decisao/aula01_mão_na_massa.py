### 🛠️ Prática do Aluno (Mão na Massa)
#Declare variáveis para representar:
#* `media_aluno` (nota de 0 a 10)
#* `frequencia_percentual` (frequência de 0 a 100)

#Crie uma expressão lógica que verifique se o aluno foi aprovado (critério da escola: média maior ou igual a 6.0 **E** frequência maior ou igual a 75%).
print("Seja bem vindo ao verificador de aprovação!!")
print("")
aluno = input("Digite seu nome: ")
media_aluno = float(input("Digite a sua média de aluno: "))
frequencia_percentual = int(input("Digite o seu percentual de frequência de aluno: "))
if media_aluno >= 6 <= 10 and frequencia_percentual >= 75 <= 100:
    print(f"Parabéns {aluno} você foi Aprovado!!!")
elif media_aluno < 6 and frequencia_percentual < 75:
    print(f"{aluno} infelizmente você foi Reprovado.")
elif media_aluno < 6 and frequencia_percentual >= 75 <= 100:
    print(f"{aluno} infelizmente você foi Reprovado por sua nota.")
elif media_aluno >= 6 <= 10 and frequencia_percentual < 75:
    print(f"{aluno} infelizmente você foi Reprovado por sua frequência.")
else:
    print("Erro.....  Tente novamente.")
