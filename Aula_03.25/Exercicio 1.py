# Exercicios 1.
# 1 - Sistema de login com nível de acesso. solicite usuário e senha. Se usuário é igual a admin, crie uma estrutura de condição aninhada para solicitar senha e se a mesma for '1234', mostre que o usuário terá acesso total. Caso o usuário insira a senha incorreta, mostre senha incorreta. Caso usuário insira usuário incorreto, mostre usuário incorreto
 
Usuario = input("Digit seu usuario: ")
 
if Usuario == 'admin':
    senha = (input("Digite sua senha: "))
 
    if senha == '1234':
        print("Acesso sucedido")
    else:
        print("Acesso negado, sua senha esta incorreta")
 
else:
    print("Seu usuario esta incorreto")