import pandas as pd

dados = {
    'nome': ['ana', 'Bruno', 'Carlos', 'Diana', 'Eduardo']
    'idade': [23, 35, 29, 40, 18],
    'Salario': [2000, 5000, 3000, 7000, 1500]
}

df = pd.dataFrame(dados)

# Ex.2

for i in range(len(df)):
    if df.loc[i, 'idade'] > 30:
        print(df.loc[i, 'nome'])

# Ex.3
for i in range(len(df)):
    
    salario = df.loc[i, 'Salario']
    
    if salario < 3000:
        print("Baixo")
    elif salario < 6000:
        print("Médio")
    else:
        print("Alto")
        
# Ex.4 - Acumular valores

soma =0

for i in df['salario']:
    soma += i
    
print(soma)

# Ex.5 - Exemplo com While

i = 0

while i < len(df):
    print(df.loc[i, 'nome'])
    i += 1