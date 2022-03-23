import os

CODIGO_VAZIO = 0
CODIGO_JOGADOR1 = 1
CODIGO_JOGADOR2 = -1

SIMBOLO_VAZIO = '-'
SIMBOLO_JOGADOR1 = 'X'
SIMBOLO_JOGADOR2 = 'O'

JOGADOR1_GANHOU = 3
JOGADOR2_GANHOU = -3

quadro = [
    [CODIGO_VAZIO, CODIGO_VAZIO, CODIGO_VAZIO],
    [CODIGO_VAZIO, CODIGO_VAZIO, CODIGO_VAZIO],
    [CODIGO_VAZIO, CODIGO_VAZIO, CODIGO_VAZIO],
]

ganhador = None

jogador_atual = SIMBOLO_JOGADOR1


def pegar_simbolo_jogador(jogador: int):
    if jogador == CODIGO_JOGADOR1:
        return SIMBOLO_JOGADOR1
    elif jogador == CODIGO_JOGADOR2:
        return SIMBOLO_JOGADOR2
    else:
        return SIMBOLO_VAZIO


def pegar_codigo_jogador(simbolo: str):
    if simbolo == SIMBOLO_JOGADOR1:
        return CODIGO_JOGADOR1
    elif simbolo == SIMBOLO_JOGADOR2:
        return CODIGO_JOGADOR2
    else:
        return CODIGO_VAZIO


def imprimir_quadro():
    os.system('cls||clear')  # Limpa a tela
    for posicao_x, linha in enumerate(quadro):
        for posicao_y, coluna in enumerate(linha):
            if pegar_simbolo_jogador(coluna) == '-':
                print(f'{posicao_x}.{posicao_y}', end='\t')
            else:
                print(pegar_simbolo_jogador(coluna), end='\t')
        print('\n')


def verificar_ganhador():
    # Verifica se algum jogador ganhou na horizontal
    for linha in quadro:
        soma = 0
        for coluna in linha:
            soma += coluna
        if soma == JOGADOR1_GANHOU:
            return SIMBOLO_JOGADOR1
        elif soma == JOGADOR2_GANHOU:
            return SIMBOLO_JOGADOR2

    # Verifica se algum jogador ganhou na vertical
    for coluna in range(3):
        soma = 0
        for linha in quadro:
            soma += linha[coluna]
        if soma == JOGADOR1_GANHOU:
            return SIMBOLO_JOGADOR1
        elif soma == JOGADOR2_GANHOU:
            return SIMBOLO_JOGADOR2

    # Verifica se algum jogador ganhou na diagonal
    soma = 0
    for i in range(3):
        soma += quadro[i][i]
    if soma == JOGADOR1_GANHOU:
        return SIMBOLO_JOGADOR1
    elif soma == JOGADOR2_GANHOU:
        return SIMBOLO_JOGADOR2

    # Verifica se algum jogador ganhou na diagonal inversa
    soma = 0
    for i in range(3):
        soma += quadro[i][2 - i]
    if soma == JOGADOR1_GANHOU:
        return SIMBOLO_JOGADOR1
    elif soma == JOGADOR2_GANHOU:
        return SIMBOLO_JOGADOR2

    # Verifica se deu empate
    empate = 0
    for linha in quadro:
        if 0 not in linha:
            empate += 1
    if empate == JOGADOR1_GANHOU:
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
    quadro[x][y] = pegar_codigo_jogador(jogador_atual)
    if jogador_atual == SIMBOLO_JOGADOR1:
        jogador_atual = SIMBOLO_JOGADOR2
    else:
        jogador_atual = SIMBOLO_JOGADOR1
    ganhador = verificar_ganhador()

imprimir_quadro()

print('\n')
if ganhador != CODIGO_VAZIO:
    print(f'O jogador {ganhador} ganhou!')
else:
    print('Deu velha!')
print('Fim de jogo!')
