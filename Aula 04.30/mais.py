try:
    # Bloco que pode gerar erro
except TipoDo Erro:
    # O que fazer se o erro acontecer

#Ex 1.    
try:
    numero = int(input("Digite um número inteiro: "))
    print(f"Você digitou {numero}")
except ValueError:
    print("Isso não é um número inteiro válido")
    
    

#Ex 2.

try:
    a = int(input("Insira um número: "))   
    b = int(input("Insira um número: ")) 
    soma = a + b
    subtracao = a - b
    divisao = a / b
    multiplicacao = a + b
    print(soma)
    print(subtracao)
    print(divisao)
    print(multiplicacao)
    
except ZeroDivisionError:
    print("Não é permitido dividir por zero! ")
    
    
    
    
    
#EX 3.    

def entrada_numero():
    
try:
    numero = int(input("Digite um número inteiro: "))
    print(f"Você digitou {numero}")
except ValueError:
    print("Isso não é um número inteiro válido")    
    
entrada_numero()

# Ex 4.
          0   1   2   3   4  5   6  7
lista = [10, 20, 30, 40, 50]

try:
    indice = int(input("Digite um indice para acessar um valor da lista: "))
    print(f"O valor no indice {indice} é: {lista[indice]}")
    
except IndexError:
    print("Este indice não existe na lista!")
    
except ValueError:
    print("Precisa inserir um número!")


## Exercicio 1

# Crie um algoritimo para tranformar temperatura em graus celsius para fahrenheit.
#Utilize try/except

fahrenheit = (celsius * 9/5) + 32

try:
    celsius = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"A temperatura em Fahrenheit é: {fahrenheit}")
except ValueError:
    print("Por favor, digite um número válido.")
    
    
    

## Exercicio 2

# Crie um algoritimo para solicitar tipo de figura para calcular a respectiva area.

# Se 1 = circulo, se 2 = retangulo. Ao escolher a respectiva figura, solicite os dados
# necessários para calcular a area.