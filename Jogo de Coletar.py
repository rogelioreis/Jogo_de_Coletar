import random
import curses

# Tamanho do mapa
MAPA_LARGURA = 120
MAPA_ALTURA = 29

# Caracteres do mapa
ITEM = "•"
VAZIO = " "

class Jogador:
    def __init__(self):
        self.posicao = (0, 0)
        self.pontuacao = 0
        self.caractere = "@"

def gerar_mapa():
    # Matriz do mapa vazio
    mapa = []
    for _ in range(MAPA_ALTURA):
        linha = []
        for _ in range(MAPA_LARGURA):
            linha.append(VAZIO)
        mapa.append(linha)

    for _ in range(30):
        x = random.randint(0, MAPA_LARGURA - 1)
        y = random.randint(0, MAPA_ALTURA - 1)
        mapa[y][x] = ITEM
    return mapa

def desenhar_mapa(stdscr, mapa, jogador):
    stdscr.addstr(0, 0, f"Pontuação: {jogador.pontuacao}")
    for y in range(MAPA_ALTURA):
        for x in range(MAPA_LARGURA):
            caractere = mapa[y][x]
            try:
                stdscr.addch(y+1, x, caractere)
            except curses.error:
                pass  # Ignora erros ao desenhar na tela
    stdscr.refresh()

def mover_jogador(mapa, jogador, movimento):
    x, y = jogador.posicao
    novo_x, novo_y = x, y

    if (movimento == "w") and (y > 0):
        novo_y -= 1
    elif (movimento == "s") and (y < MAPA_ALTURA - 1):
        novo_y += 1
    elif (movimento == "a") and (x > 0):
        novo_x -= 1
    elif (movimento == "d") and (x < MAPA_LARGURA - 1):
        novo_x += 1

    if mapa[novo_y][novo_x] == ITEM:
        jogador.pontuacao += 1
    
    mapa[y][x] = VAZIO
    mapa[novo_y][novo_x] = jogador.caractere
    jogador.posicao = (novo_x, novo_y)

    return jogador.posicao
    
def main(stdscr):

    curses.curs_set(0) # Oculta o cursor
    stdscr.nodelay(True) # Torna o teclado não-bloqueante

    mapa = gerar_mapa()
    jogador = Jogador() # Jogador inicia no topo da tela
    mapa[jogador.posicao[1]][jogador.posicao[0]] = jogador.caractere

    while True:
        stdscr.clear()
        desenhar_mapa(stdscr, mapa, jogador)

        key = stdscr.getch()

        if key == ord("q"): # Tecla q para sair do jogo
            break
        elif key in [ord("w"), ord("s"), ord("a"), ord("d")]:
            mover_jogador(mapa, jogador, chr(key))

if __name__ == "__main__":
    curses.wrapper(main)