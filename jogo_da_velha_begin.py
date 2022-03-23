quadro = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]

jogadores_simbolos = {
    0: '-',  # Nenhum jogador
    1: 'X',  # Jogador X
    -1: 'O'  # Jogador Y
}

simbomolos_jogadores = {
    'X': 1,
    'O': -1
}

ganhador = None

jogador_atual = 'X'


def imprimir_quadro():
    print('\n')
    for x, linha in enumerate(quadro):
        for y, coluna in enumerate(linha):
            if jogadores_simbolos[coluna] == '-':
                print(f'{x}.{y}', end='\t')
            else:
                print(jogadores_simbolos[coluna], end='\t')
        print('\n')


def verificar_ganhador():
    # Verifica se algum jogador ganhou na horizontal

    # Verifica se algum jogador ganhou na vertical

    # Verifica se algum jogador ganhou na diagonal

    # Verifica se algum jogador ganhou na diagonal inversa

    # Verifica se deu empate

    return None


while ganhador is None:  # Enquanto não houver ganhador
    imprimir_quadro()
    jogada = input(
        f'Jogador {jogador_atual} - escolha uma posição x.y (ex: 1.2): '
    )
    # Quebrar a string em 2 partes, Ex.: 1.2 -> 1 e 2

    # Converter a string para inteiro

    # Preencher o quadro com o simbolo do jogador nas posições x e y

    # Inverter o jogador atual

    # Verificar se algum jogador ganhou

print('\n')

if ganhador != 0:  # Se jogador == 0 é porque deu empate (Velha)
    print(f'O jogador {ganhador} ganhou!')
else:
    print('Deu velha!')

print('Fim de jogo!')
