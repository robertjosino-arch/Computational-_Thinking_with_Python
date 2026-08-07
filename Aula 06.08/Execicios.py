#----AULA DO DIA 05/08------------------------------------------------------------------

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

#----------------------------------------------------------------------------------------------------- 

#----AULA DO DIA 05/08------------------------------------------------------------------

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

#----------------------------------------------------------------------

#Crie um algoritmo para solicitar marca de carro, versão do carro, ano, cor, IPVA pago. Solicite 4 informações para cada tipo de informação. Deixe cada informação em uma sublista. Utilize while ou for para solicitar as informações repetidas.

#----------------------------------------------------------------------

carros = []

for i in range(4):
   print(f"\n--- Carro {i + 1} ---")
   marca = input("Insira a marca do carro: ")
   versao = input("Insira a versão do carro: ")
   ano = input("Insira o ano do carro: ")
   cor = input("Insira a cor do carro: ")
   ipva_pago = input("IPVA pago (Sim ou Não): ")
   sublista = [marca, versao, ano, cor, ipva_pago]
   carros.append(sublista)

print("\n--- Lista de carros cadastrados ---")
for carro in carros:
   print(carro)

#----------------------------------------------------------------------

carros = []
contador = 0

while contador < 4:
   print(f"\n--- Carro {contador + 1} ---") # O professor até usou esse exemplo depois, mas ele não usou essa linha
   marca = input("Marca do carro: ")
   versao = input("Versão do carro: ")
   ano = input("Ano: ")
   cor = input("Cor: ")
   ipva_pago = input("IPVA pago (Sim/Não): ")
   
   sublista = [marca, versao, ano, cor, ipva_pago]
   carros.append(sublista)
   contador += 1

print("\n--- Lista de carros cadastrados ---")
for carro in carros:
   print(carro)

#----------------------------------------------------------------------
 
# Versão correta do exercicio que o professor passou

dados = [[], [], [], [], []]
contador = 0

while contador < 4:
    marca = input("Digite marca do carro: ")
    versao = input("Digite versão do carro: ")
    ano = int(input("Digite ano do carro: "))
    cor = input("Digite cor do carro: ")
    ipva = input("Digite se IPVA foi pago ou não: ")

    dados[0].append(marca)
    dados[1].append(versao)
    dados[2].append(ano)
    dados[3].append(cor)
    dados[4].append(ipva)
    contador += 1

print(dados)


