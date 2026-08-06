lista_nomes = []
lista_idades = []
lista_sexo = []
for i in range(2):
   print(f"\nDados da {i + 1}ª pessoa:")
   nome = input("Digite o nome: ")
   lista_nomes.append(nome)
   idade = int(input("Digite a idade: "))
   lista_idades.append(idade)
   sexo = input("Digite M para masculino e F para feminino: ")
   lista_sexo.append(sexo)
print(lista_nomes)
print(lista_idades)
print(lista_sexo)

#----------------------------------------------------------------------

lista_nomes = []
lista_idades = []
lista_sexo = []
resultado = []

for i in range(2):
   print(f"\nDados da {i + 1}ª pessoa:")
   nome = input("Digite o nome: ")
   idade = int(input("Digite a idade: "))
   sexo = input("Digite M para masculino e F para feminino: ")
   
   resultado.append([nome, idade, sexo])
   
print(resultado)

#----------------------------------------------------------------------

## Exemplo do Prof

lista_completa = []

 
for k in range(2):
   nome = input("Digite o nome: ")
   idade = int(input("Digite a idade: "))
   sexo = input("Digite M para masculino e F para feminino: ")
   
   lista = [nome, idade, sexo]
   lista_completa.append(lista)
   print(lista_completa)