## 🛠️ Prática do Aluno (Mão na Massa)
#Agora é a sua vez! Crie 4 variáveis para cadastrar um novo produto no estoque de informática da escola:
#1. `nome_produto` (texto)
#2. `quantidade_estoque` (inteiro)
#3. `preco_unitario` (ponto flutuante)
#4. `disponivel_para_venda` (booleano)

#Em seguida, exiba o valor de cada uma e seu respectivo tipo usando `print()` e `type()`.


nome_produto = input("Digite o nome do produto: ")
quantidade_estoque = int(input("Digite a quantidade de produtos em estoque: "))
preco_unitario = float(input("Digite o preço unitário do produto: "))
disponivel_para_venda = bool(input("Está disponivel pra venda?: "))

print(type(nome_produto))
print(type(quantidade_estoque))
print(type(preco_unitario))
print(type(disponivel_para_venda))