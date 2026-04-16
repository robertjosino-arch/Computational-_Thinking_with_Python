# Ex.3

entrada = int(input('Digite um número: '))

soma = 0 

while entrada > 0: 
    soma += entrada
    print(soma)
    entrada = int(input('Digite um número: '))


# Ex.5

soma = 0
num = 3

while num <= 5:
    soma += num
    num += 1 
    print(soma)

while num <= 5:
    soma = soma + num
    num = num + 1 
    print(soma)   

# Ex.4

realizado = False

while not realizado:
    entrada = int(input('Digite um valor: '))

    if entrada == 000:
        realizado = True
    else:
        print:(entrada)

