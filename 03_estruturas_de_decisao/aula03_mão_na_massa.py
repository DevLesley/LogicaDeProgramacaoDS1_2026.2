## 🛠️ Prática do Aluno (Mão na Massa)
#Construa um menu interativo para o sistema da biblioteca da escola:
#* Opção 1: Consultar livro
#* Opção 2: Realizar empréstimo
#* Opção 3: Devolver livro
#* Qualquer outra opção: Mensagem de "Opção Não Encontrada".

from ast import match_case


opcao = int(input("Digite a opção desejada (1, 2 ou 3): "))
match opcao:
    case 1:
        print("A opção escolhida foi: Consultar livro..")
    case 2:
            print("A opção escolhida foi: Emprestimo..")
    case 3:
                print("A opção escolhida foi: Devolver livro..")
    case _:
                print("opção inválida..") 
    