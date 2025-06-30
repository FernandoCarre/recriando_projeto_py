import os

restaurantes = [{'nome':'Fernando Sushi', 'categoria':'Japonesa', 'ativo': False,
                 'nome':'Neguinha Marmita', 'categoria': 'Marmita', 'ativo': True}]

def exibir_nome_do_programa():
    print('''
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
─██████████████─██████████████─████████████████───████████████████───██████████████────██████████████─████████──████████─██████████████─████████████████───██████████████─██████████████─██████████████─
─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░░░██───██░░░░░░░░░░░░██───██░░░░░░░░░░██────██░░░░░░░░░░██─██░░░░██──██░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░░░██───██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
─██░░██████████─██░░██████░░██─██░░████████░░██───██░░████████░░██───██░░██████████────██░░██████████─████░░██──██░░████─██░░██████░░██─██░░████████░░██───██░░██████████─██░░██████████─██░░██████████─
─██░░██─────────██░░██──██░░██─██░░██────██░░██───██░░██────██░░██───██░░██────────────██░░██───────────██░░░░██░░░░██───██░░██──██░░██─██░░██────██░░██───██░░██─────────██░░██─────────██░░██─────────
─██░░██─────────██░░██████░░██─██░░████████░░██───██░░████████░░██───██░░██████████────██░░██████████───████░░░░░░████───██░░██████░░██─██░░████████░░██───██░░██████████─██░░██████████─██░░██████████─
─██░░██─────────██░░░░░░░░░░██─██░░░░░░░░░░░░██───██░░░░░░░░░░░░██───██░░░░░░░░░░██────██░░░░░░░░░░██─────██░░░░░░██─────██░░░░░░░░░░██─██░░░░░░░░░░░░██───██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
─██░░██─────────██░░██████░░██─██░░██████░░████───██░░██████░░████───██░░██████████────██░░██████████───████░░░░░░████───██░░██████████─██░░██████░░████───██░░██████████─██████████░░██─██████████░░██─
─██░░██─────────██░░██──██░░██─██░░██──██░░██─────██░░██──██░░██─────██░░██────────────██░░██───────────██░░░░██░░░░██───██░░██─────────██░░██──██░░██─────██░░██─────────────────██░░██─────────██░░██─
─██░░██████████─██░░██──██░░██─██░░██──██░░██████─██░░██──██░░██████─██░░██████████────██░░██████████─████░░██──██░░████─██░░██─────────██░░██──██░░██████─██░░██████████─██████████░░██─██████████░░██─
─██░░░░░░░░░░██─██░░██──██░░██─██░░██──██░░░░░░██─██░░██──██░░░░░░██─██░░░░░░░░░░██────██░░░░░░░░░░██─██░░░░██──██░░░░██─██░░██─────────██░░██──██░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
─██████████████─██████──██████─██████──██████████─██████──██████████─██████████████────██████████████─████████──████████─██████─────────██████──██████████─██████████████─██████████████─██████████████─
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────''')
def exibir_opcoes():
    print('\n1- Cadastrar restaurante\n'
      '2- Listar restaurante\n'
      '3- Alternar restaurante\n'
      '4- Encerrar aplicativo\n')
    
def retornar_menu_principal():
     input('\nTecle enter para para retornar ao menu principal ')
     main()
    
def cadastro_restaurante():
    os.system('cls')
    print('Cadastro de restaurante')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input('Digite a categoria do restaurante: ')
    restaurantes.append(nome_do_restaurante)
    restaurantes.append(categoria)
    print(f'O restaurante {nome_do_restaurante} de {categoria} foi cadastrado com sucesso!')

    retornar_menu_principal()

def exibir_restaurantes():
    os.system('cls')
    print('Lista de restaurantes cadastrados:\n')

    for restaurante in restaurantes:
        print(restaurante)

    retornar_menu_principal()

def alternar_estado_restaurante():
    os.system('cls')
    print('Alternar o estado do restaurante')

    nome_do_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_do_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            print('Deu certo')

        


    
def finalizar_app():
    os.system('cls')
    print('Aplicativo encerrado.')    

def opcao_invalida():
    os.system('cls')
    input('Opção inválida! Aperte enter para retornar ao menu principal ')
#a def precisa vir antes de ser chamada, caso contrário não funcionária no código

def menu_escolhas():
    try:
        escolha_opcao = int(input('Escolha uma opção: '))
        #eu botei ele fora e o except não funcionava

        if escolha_opcao == 1:
            cadastro_restaurante()
        elif escolha_opcao == 2:
            exibir_restaurantes()
        elif escolha_opcao == 3:
            alternar_estado_restaurante()
        elif escolha_opcao == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    menu_escolhas()

#acertei de first try! Uau.
if __name__ == '__main__':
    main()



