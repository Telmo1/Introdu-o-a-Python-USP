def usuario_escolhe_jogada(n, m):
    jogada = 0
    while jogada <= 0 or jogada > m or jogada > n:
        jogada = int(input(f"Quantas peças você quer tirar (máximo {min(m, n)} peças)? "))
        if jogada <= 0 or jogada > m or jogada > n:
            print(f"Jogada inválida. Tente novamente.")
    return jogada

def computador_escolhe_jogada(n, m):
    if n % (m+1) == 0:
        return m
    else:
        return n % (m+1)

def partida():
    n = int(input("Digite o número de peças: "))
    m = int(input("Digite o número máximo de peças por jogada: "))

    computador_comeca_jogo = computador_comeca(n, m)

    while n > 0:
        if computador_comeca_jogo:
            jogada = computador_escolhe_jogada(n, m)
            print(f"O computador tirou {jogada} peças.")
            n -= jogada
            computador_comeca_jogo = False
        else:
            jogada = usuario_escolhe_jogada(n, m)
            n -= jogada
            computador_comeca_jogo = True

        print(f"Agora restam {n} peças no tabuleiro.\n")

    if computador_comeca_jogo:
        print("Você ganhou!")
    else:
        print("O computador ganhou!")

def computador_comeca(n, m):
    if (n % (m+1)) == 0:
        print("Você começa!")
        return False
    else:
        print("Computador começa!")
        return True

    
partida()
