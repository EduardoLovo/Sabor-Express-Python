import os

restaurantes = [
    {'nome': 'Don Chilli', 'categoria': 'Mexicano', 'ativo': False},
    {'nome': 'Tokyo Roll', 'categoria': 'Japonesa', 'ativo': True},
    {'nome': 'Pizza Suprema', 'categoria': 'Italiana', 'ativo': False}
]


def exibir_nome_do_programa():
    '''Essa funçao é responsavel por exibir o nome do app'''

    print('''
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    ''')


def exibir_opcoes():
    '''Essa função é responsavel por exibir as opções do app'''

    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')


def finalizar_app():
    '''Essa função é responsavel por finalizar a aplicação'''
    exibir_subtitulo('Finalizando app')


def voltar_ao_menu_principal():
    '''Essa função é responsavel por voltar ao menu principal do app
    
    Inputs:
    - Qualquer tecla
    '''

    input('\nDigite uma tecla para voltar ao menu principal ')
    main()


def opcao_invalida():
    '''Essa função é responsavel por retornar mensagem de opçao invalida, caso o usuario escolha uma opção inexistente'''

    print('Opção invalida!\n')
    voltar_ao_menu_principal()


def exibir_subtitulo(texto):
    '''Essa função é responsavel por exibir o subtitulo'''

    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()


def cadastrar_novo_restaurante():
    '''Essa função é responsavel por cadastrar um novo restaurante
    
    Inputs:
    - Nome do restaurante
    - Categoria

    Output:
    - Adiciona um novo restaurante a lista de restaurantes
    '''

    exibir_subtitulo('Cadastro de novos restaurantes')

    nome_do_restaurante = input(
        'Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {
                      nome_do_restaurante}: ')

    dados_do_restaurante = {'nome': nome_do_restaurante,
                            'categoria': categoria, 'ativo': False}

    restaurantes.append(dados_do_restaurante)

    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso')
    voltar_ao_menu_principal()


def listar_restaurantes():
    '''Essa função é responsavel por listar os restaurantes'''

    exibir_subtitulo('Lista de restaurantes:')

    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'

        print(f'- {nome_restaurante.ljust(20)
                   } | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()


def alternar_estado_restaurante():
    '''Essa função é responsavel por alterar o estado dos restaurantes'''

    exibir_subtitulo('Alternando estado do restaurante')

    nome_restaurante = input(
        'Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado co sucesso' if restaurante['ativo'] else f'O restaurante {
                nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
    voltar_ao_menu_principal()


def escolher_opcoes():
    '''Essa função é responsavel pelas condiçoes para as opções do app'''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            print('Finalizando app')
        else:
            opcao_invalida()
    except:
        opcao_invalida()


def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()


if __name__ == '__main__':
    main()
