qtd_partidas = int(input())
stop = False
j = 1
x = 0

while j <= qtd_partidas and not stop:
    qtd_rodadas = int(input())
    placar_adversario = 0
    placar_equipe = 0
    if j - qtd_partidas == 0:
        print(f"Tá na hora da grande final! Esse jogo terá {qtd_rodadas} rodada(s).")
        while x < qtd_rodadas:
            habilidade_jogador = int(input())
            habilidade_adversario = int(input())
            if habilidade_adversario > habilidade_jogador:
                placar_adversario += 1
            elif habilidade_adversario == habilidade_jogador:
                placar_equipe += 1
            else:
                placar_equipe += 1
            x += 1
        if placar_equipe > placar_adversario:
            print(f"Fim de jogo! O placar foi {placar_equipe}x{placar_adversario}")
            print("É CAMPEÃO! O TIME DE IP/P1 GARANTIU A TAÇA!")
            stop = True
        else:
            print(f"Fim de jogo! O placar foi {placar_equipe}x{placar_adversario}")
            print("Ah não!! Chegaram tão longe mas não foi dessa vez. :(")
            stop = True
    else:
        print(f"Vai começar a {j}º partida. Esse jogo terá {qtd_rodadas} rodada(s).")
        placar_adversario = 0
        placar_equipe = 0
        i = 0
        while i < qtd_rodadas and not stop:
            habilidade_jogador = int(input())
            habilidade_adversario = int(input())
            if habilidade_adversario > habilidade_jogador:
                placar_adversario += 1
            if habilidade_adversario == habilidade_jogador:
                placar_equipe += 1
            if habilidade_adversario < habilidade_jogador:
                placar_equipe += 1
            i += 1
    if not stop:
        print(f"Fim de jogo! O placar foi {placar_equipe}x{placar_adversario}")
    if placar_equipe == placar_adversario and not stop:
        print("Não foi dessa vez! Treinar pro ano que vem!")
        stop = True
    elif placar_equipe - placar_adversario >= 5 and qtd_partidas - j != 0 and not stop:
        print("QUE GOLEADAAAA!!! Essa vitória fez os outros times desistirem e a equipe de IP/P1 é a campeã!") # antes da final
        stop = True
    else:
        if not stop:
            print("Vamos para próxima fase!")
    j += 1
