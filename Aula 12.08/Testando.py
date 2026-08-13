dicionario = {

    'time': ["a", "b", "c"],

    'vitorias' : [10, 20, 30],

    'Estados' : ["rj", "sp", "ce"]

}

print(dicionario)

import pandas as pd

dados = pd.DataFrame(dicionario)

dados

#mostra em planilha

###################################################################

cliente = {}

cliente["nome"] = input("Nome: ")
cliente["idade"] = int(input("Idade: "))
cliente["cidade"] = input("Cidade: ")

print(cliente)

###################################################################

cliente = {}
cliente["nome"] = input("Nome: ")
cliente["idade"] = int(input("Idade: "))
cliente["cidade"] = input("Cidade: ")

print(cliente)

###################################################################

produto = {"preco": 800, "estoque": 3}
   
if produto["preco"] > 1000:
   categoria = "Alto valor"

else:
  categoria = 'preço baixo'

print(categoria)
