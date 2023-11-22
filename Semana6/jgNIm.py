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
        return "Você ganhou!"
    else:
        return "Fim do jogo! O computador ganhou!"

def computador_comeca(n, m):
    if (n % (m+1)) == 0:
        print("Você começa!")
        return False
    else:
        print("Computador começa!")
        return True

def campeonato():
    placar_usuario = 0
    placar_computador = 0

    for _ in range(3):  # Executa três partidas
        resultado_partida = partida()

        if "Você ganhou" in resultado_partida:
            placar_usuario += 1
        else:
            placar_computador += 1

    print("\nPlacar: Você {} X {} Computador".format(placar_usuario, placar_computador))

    if placar_usuario > placar_computador:
        print("Você venceu o campeonato!")
    elif placar_usuario < placar_computador:
        print("O computador venceu o campeonato!")
    else:
        print("O campeonato terminou em empate!")

def escolha_modo_jogo():
    while True:
        print("Escolha o modo de jogo:")
        print("1 - Partida única")
        print("2 - Campeonato")
        escolha = input("Digite 1 ou 2 para escolher o modo de jogo: ")

        if escolha == "1":
            partida()
            break
        elif escolha == "2":
            campeonato()
            break
        else:
            print("Escolha inválida. Por favor, digite 1 ou 2.")

escolha_modo_jogo()



