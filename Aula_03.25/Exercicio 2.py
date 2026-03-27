#2 Classificação de idade. solicite idade, se idade for maior ou igual a 18, crie uma estrutura de condição aninhada para verificar se idade é maior ou igual a 60, se for, mostre que é idoso, senão, mostre que é adulto. Se idade for maior ou igual a 12, adolescente, caso contrário, criança.
 
Idade = int(input("Digite sua idade: "))
 
if Idade >= 18:
    if Idade >= 60:
        print("Você é idoso")
    else:
        print("Aduto")
else:
    if Idade >= 12:
        print("Você é adolescente!")
    else:
        print("Criança")