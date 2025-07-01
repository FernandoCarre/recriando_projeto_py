import os

restaurantes = [{'nome':'Fernando Sushi', 'categoria':'Japonesa', 'ativo': False},
                 {'nome':'Neguinha Marmita', 'categoria': 'Marmita', 'ativo': True}]
#porque eu não fechei as chaves de cada dicionário a lista considerou apenas o último dicionário.

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
    
def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()
    
def retornar_menu_principal():
     input('\nTecle enter para para retornar ao menu principal ')
     main()
    
def cadastro_restaurante():
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
    exibir_subtitulo('Lista de restaurantes cadastrados:')
    for restaurante in restaurantes:
        ###-meu erro corrigo
        nome_do_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = restaurante['ativo']
        print(f'- {nome_do_restaurante} | {categoria} | {ativo}')
        #print(f'{restaurante['nome'], restaurante['categoria'], restaurante['ativo']}')
        ###
    retornar_menu_principal()

def alternar_estado_restaurante():
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