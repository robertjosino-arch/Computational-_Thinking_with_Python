Match/case 
comando = 'fiap'
comando = 'start'
if comando == ' start':
    print('iniciar')
elif comando == 'stop':
    print('parar')
else: 
    print('Erro')
############################
match comando:
    case "start":
        print(' iniciar')
    case 'stop':
    print('parar')
    case _:
        print('Erro')
##################################
opcao = input('Insira 1 ou 2:')
match opcao:
    case '1':
        print('cadastrar!')
    case '2':
        print('Listar!')
    case_:
        print("Valor invalida!")
###############################
dados = ['produtos', 'arroz', 10]
match dados:
    case ('produtos', asd, qtd):
        print(f"{asd} - {qtd}")
    case _:
        print("Format inalido!")
#########################################
dados = ['produtos', 'arroz', 10]
match dados:
    case ('nome', produtos, qtd):
        print(f"{produtos} - {qtd}")
    case _:
        print("Format inalido!")
##########################
 
sem = int(input("Digite um numero de 1 a 7: "))
match sem: 
    case 1:
        print("segunda")
    case "2":
        print("tercou")
    case "3":
        print("quartou")
    case "4":
        print("quinta")
    case "5":
        print("sexta")
    case "6":
        print("sabado")
    case "7":
        print("domingo") 
####################################
 
nome_da_uni= ("Me informe o nome da sua faculdade:")
match
 