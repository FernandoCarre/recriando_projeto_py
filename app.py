import os

restaurantes = [{'nome':'Fernando Sushi', 'categoria':'Japonesa', 'ativo': False},
                 {'nome':'Neguinha Marmita', 'categoria': 'Marmita', 'ativo': True}]
#porque eu não fechei as chaves de cada dicionário a lista considerou apenas o último dicionário.

def exibir_nome_do_programa():
    '''Função responsável por mostrar o nome do programa'''
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
    '''Função responsável por mostrar as opções disponíveis'''
    print('\n1- Cadastrar restaurante\n'
      '2- Listar restaurante\n'
      '3- Alternar restaurante\n'
      '4- Encerrar aplicativo\n')
    
def exibir_subtitulo(texto):
    '''Função responsável por mostrar o título de cada opção escolhida'''
    linha = '*' * len(texto)
    os.system('cls')
    print(linha)
    print(texto)
    print(linha)
    print()
    
def retornar_menu_principal():
     input('\nTecle enter para para retornar ao menu principal ')
     main()
    
def cadastro_restaurante():
    '''Função responsável por cadastrar os restaurantes'''
    exibir_subtitulo('Cadastro de restaurante:')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    ###-meu erro corrigido
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria':categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    ###
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    retornar_menu_principal()

def exibir_restaurantes():
    '''Função responsável por listar os restaurantes'''
    exibir_subtitulo('Lista de restaurantes cadastrados:')
    print(f'{'Nome'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
    #Por algum motivo não estava funcionando, fui conferir com o original e estava igual...
    #O motivo do erro é porque eu não encerrei o programa e fiquei "runando" ele achando que isso daria reboot.
    
    for restaurante in restaurantes:
        
        nome_do_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = restaurante['ativo']
        print(f'- {nome_do_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
       
    retornar_menu_principal()

def alternar_estado_restaurante():
    '''Função responsável por mudar o estado do restaurante'''
    exibir_subtitulo('Alternar o estado do restaurante:')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_do_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            ###
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_do_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_do_restaurante} foi desativado com sucesso!'
            print(mensagem)
    if not restaurante_encontrado:
            print('O restaurante não foi encontrado.')
            ###
    retornar_menu_principal()
          
def finalizar_app():
    '''Função responsável por encerrar o aplicativo'''
    os.system('cls')
    print('Aplicativo encerrado.')    

def opcao_invalida():
    '''Função responsável por mostrar uma mensagem de erro'''
    os.system('cls')
    input('Opção inválida! Aperte enter para retornar ao menu principal ')
    main()
#a def precisa vir antes de ser chamada, caso contrário não funcionária no código

def menu_escolhas():
    '''Função responsável por direcionar o usuário para a opção escolhida'''
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
    '''Função responsável por iniciar as funções e tornar a manutenção do código mais fácil'''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    menu_escolhas()

#acertei de first try! Uau.
if __name__ == '__main__':
    main()