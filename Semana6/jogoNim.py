def computador_comeca(n, m):
    if n % (m+1) == 0:
        print("Você começa!")
        return False
    else:
        print("Computador começa!")
        return True

def turno_computador(n, m):
    if n <= m:
        return n
    elif n % (m+1) == 0:
        return m
    else:
        return n % (m+1)

def turno_jogador():
    return int(input("Quantas peças você quer tirar? "))

def partida():
    n = int(input("Digite o número de peças: "))
    m = int(input("Digite o número máximo de peças por jogada: "))

    computador_comeca_jogo = computador_comeca(n, m)

    while n > 0:
        if computador_comeca_jogo:
            jogada = turno_computador(n, m)
            print(f"O computador tirou {jogada} peças.")
            n -= jogada
            computador_comeca_jogo = False
        else:
            jogada = turno_jogador()
            if jogada > m or jogada <= 0 or jogada > n:
                print("Jogada inválida. Tente novamente.")
                continue
            n -= jogada
            computador_comeca_jogo = True

        print(f"Agora restam {n} peças no tabuleiro.\n")

    if computador_comeca_jogo:
        print("Você ganhou!")
    else:
        print("O computador ganhou!")

partida()
