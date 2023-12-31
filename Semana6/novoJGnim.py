def computador_escolhe_jogada(n, m):
    if n % (m + 1) == 0:
        return m
    else:
        return n % (m + 1)

def usuario_escolhe_jogada(n, m):
    jogada = 0
    while jogada <= 0 or jogada > m or jogada > n:
        jogada = int(input(f"Quantas peças você quer tirar (máximo {min(m, n)})? "))
        if jogada <= 0 or jogada > m or jogada > n:
            print(f"Jogada inválida. Tente novamente.")
    return jogada

def partida():
    n = int(input("Digite o número de peças: "))
    m = int(input("Digite o número máximo de peças por jogada: "))

    computador_comeca_jogo = (n % (m + 1)) != 0

    print("\n**** Rodada Inicial ****")
    while n > 0:
        if computador_comeca_jogo:
            jogada = computador_escolhe_jogada(n, m)
            n -= jogada
            computador_comeca_jogo = False
            print(f"O computador tirou {jogada} peças.")
        else:
            jogada = usuario_escolhe_jogada(n, m)
            n -= jogada
            computador_comeca_jogo = True
            print(f"Você tirou {jogada} peças.")

        print(f"Agora restam {n} peças no tabuleiro.\n")

    if computador_comeca_jogo:
        print("Você ganhou!")
        return "usuario"
    else:
        print("Fim do jogo! O computador ganhou!")
        return "computador"

def campeonato():

    placar_usuario = 0
    placar_computador = 0

    for _ in range(3):  
        resultado_partida = partida()

        if resultado_partida == "usuario":
            placar_usuario += 1
        else:
            placar_computador += 1

    print("\n**** Placar do Campeonato ****")
    print(f"Você {placar_usuario} X {placar_computador} Computador")

    if placar_usuario > placar_computador:
        print("Você venceu o campeonato!")
    elif placar_usuario < placar_computador:
        print("O computador venceu o campeonato!")
    else:
        print("O campeonato terminou em empate!")

def escolhe_modo_jogo():
    while True:
        modo = int(input("Bem-vindo ao jogo do NIM! Escolha:\n1 - para jogar uma partida isolada\n2 - para jogar um campeonato\n"))

        if modo == 1:
            partida()
            break
        elif modo == 2:
            print("Voce escolheu um campeonato!")
            campeonato()
            break
        else:
            print("Opção inválida. Tente novamente.")

escolhe_modo_jogo()
