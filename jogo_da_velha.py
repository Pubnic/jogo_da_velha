import os


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
    os.system('cls||clear')  # Limpa a tela
    for x, linha in enumerate(quadro):
        for y, coluna in enumerate(linha):
            if jogadores_simbolos[coluna] == '-':
                print(f'{x}.{y}', end='\t')
            else:
                print(jogadores_simbolos[coluna], end='\t')
        print('\n')


def verificar_ganhador():
    # Verifica se algum jogador ganhou na horizontal
    for linha in quadro:
        soma = 0
        for coluna in linha:
            soma += coluna
        if soma == 3:
            return 'X'
        elif soma == -3:
            return 'O'

    # Verifica se algum jogador ganhou na vertical
    for coluna in range(3):
        soma = 0
        for linha in quadro:
            soma += linha[coluna]
        if soma == 3:
            return 'X'
        elif soma == -3:
            return 'O'

    # Verifica se algum jogador ganhou na diagonal
    soma = 0
    for i in range(3):
        soma += quadro[i][i]
    if soma == 3:
        return 'X'
    elif soma == -3:
        return 'O'

    # Verifica se algum jogador ganhou na diagonal inversa
    soma = 0
    for i in range(3):
        soma += quadro[i][2 - i]
    if soma == 3:
        return 'X'
    elif soma == -3:
        return 'O'

    # Verifica se deu empate
    empate = 0
    for linha in quadro:
        if 0 not in linha:
            empate += 1
    if empate == 3:
        return 0

    return None


while ganhador is None:
    imprimir_quadro()
    jogada = input(
        f'Jogador {jogador_atual} - escolha uma posição x.y (ex: 1.2): '
    )
    x, y = jogada.split('.')
    x = int(x)
    y = int(y)
    quadro[x][y] = simbomolos_jogadores[jogador_atual]
    if jogador_atual == 'X':
        jogador_atual = 'O'
    else:
        jogador_atual = 'X'
    ganhador = verificar_ganhador()

print('\n')
if ganhador != 0:
    print(f'O jogador {ganhador} ganhou!')
else:
    print('Deu velha!')
print('Fim de jogo!')
