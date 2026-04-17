# 2. Crie um algoritimo para acumular 3 valores inseridos pelo usuário, print o resultado final

i = 0
contador = 0

while contador < 3:
    inserido = int(input("Insira um numero: "))
    i += inserido 
    contador += 1

    print("Resultado final! ")

#ex3. Crie um algoritimo para solicitar 5 numeros e insira este numero em uma lista

lista = []
oi = 0

while oi < 5:
    insira = int(input("Insira os numeros: "))
    oi += 1
    lista.append(insira)

    print(lista)

# Ex.4 Crie um algoritimo para solicitar 2 informações, nome unidade, após isso, print as duas inoformações

vamo = 0

while vamo < 5:
    idade = int(input("Insira os numeros: "))
    nome = input("Insira seu nome: ")
    vamo += 1

    print(idade, nome)

#6 Crie um algoritimo para somar números da lista = [23, 45, 12, 10, 25]

lista = [23, 45, 12, 10, 25]

i = 0
soma = 0

while i < len(lista): 
    soma += lista[i]
    i += 1

print("Resultado:" , soma)

#7 Crie um algoritimo para retirar das palavras os caracteres E e O da palavra engenharia de software.

# palavra = 'engenharia software'

# Utlize estrutura com while e continue.

#8. Somar ou acumular valores até digitar 0. Utilize estrutura com break.