def usuario_escolhe_jogada(n, m):
    jogada = 0
    while jogada <= 0 or jogada > m or jogada > n:
        jogada = int(input(f"Quantas peças você quer tirar (máximo {min(m, n)})? "))
        if jogada <= 0 or jogada > m or jogada > n:
            print(f"Jogada inválida. Tente novamente.")
    return jogada

def computador_escolhe_jogada(n, m):
    if n <= m:
        return n
    else:
        resto = n % (m + 1)
        if resto > 0:
            return resto
        else:
            return m

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
        return "usuario"
    else:
        print("Fim do jogo! O computador ganhou!")
        return "computador"

def computador_comeca(n, m):
    if (n % (m + 1)) == 0:
        print("Você começa!")
        return False
    else:
        print("Computador começa!")
        return True

def campeonato():
    placar_usuario = 0
    placar_computador = 0

    for _ in range(3):  # Realiza três partidas
        resultado_partida = partida()

        if resultado_partida == "usuario":
            placar_usuario += 1
        else:
            placar_computador += 1

    print("\nPlacar final do campeonato:")
    print(f"Você {placar_usuario} X {placar_computador} Computador")

    if placar_usuario > placar_computador:
        print("Você venceu o campeonato!")
    elif placar_usuario < placar_computador:
        print("O computador venceu o campeonato!")
    else:
        print("O campeonato terminou em empate!")

# Ao final do seu código, chame a função campeonato():
campeonato()

