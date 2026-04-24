# Comparação While e FOR
Ex.1
for i in range(1, 6):
    print(i)

i = 0
While i <= 5:
    print(i)
    i += 1

Ex.2

nomes = ['ana', 'paulo', 'laura']

for i in nomes:
    print(i)

i = 0
While i < len(nomes):
    print(nomes[i])
    i += 1

Ex.3 - soma de valores

lista = [10, 20, 30]

soma = 0

for valor in lista:
    soma += valor
    print(soma)

soma = 0
i = 0

while i < len(lista):
    soma += lista[i]
    i += 1
    print(soma)

Ex.4

for i in range(3):
    senha = input("Digite uma senha: ")

    if senha == '123':
        print(senha)
        break
    else:
        print("Acesso negado! ")

while True:
    senha = input("Digite uma senha: ")

    if senha == '123'
        print("Acesso permitido! ")
        break
    else:
        print("Acesso negado: ")


# Exercicios

# Para o exercicio 4, crie uma estrutura para solicitar usuario, senha utilizando for e depois com while true. 
# Mostre como quebrar a estrutura de repetição infinita do while para as duas variáveis.

