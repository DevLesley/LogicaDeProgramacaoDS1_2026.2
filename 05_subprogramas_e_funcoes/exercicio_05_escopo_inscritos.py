"""
EXERCÍCIO 05: Gestão de Escopo Global e Local
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Declare a variável global total_inscritos = 0.
Crie a função `inscrever_aluno(quantidade)` utilizando a diretiva `global`
para atualizar a variável. Demonstre o valor de total_inscritos antes e depois da chamada.
"""

# TODO: Desenvolva o algoritmo abaixo:

total_incritos = 0
def inscrever_aluno(quantidade) :
    quantidade = int(input("Digite a quantidade de alunos inscritos: "))
    total_incritos = 0
    total_inscritos_atualizado = total_incritos + quantidade
    print(f"""O total de incritos de antes é: {total_incritos}
    A nova quantidade total é: {total_inscritos_atualizado}""")
    return inscrever_aluno
quantidade = inscrever_aluno 
inscrever_aluno(quantidade)