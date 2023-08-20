time_1 = str(input())
time_2 = str(input())
i = 1
ganha1 = 0
ganha2 = 0
stop = False
while i < 6 and not stop:
    pontuacao_do_time1 = int(input())
    pontuacao_do_time2 = int(input())
    if pontuacao_do_time1 > pontuacao_do_time2:
        ganha1 += 1
        vencedor_rodada = time_1
        print("O vencedor da " + str(i) + "ª rodada foi: " + vencedor_rodada)
    else:
        ganha2 += 1
        vencedor_rodada = time_2
        print("O vencedor da " + str(i) + "ª rodada foi: " + vencedor_rodada)
    if ganha1 == 3:
        vencedor_partida = time_1
        print("O time " + vencedor_partida + " ganhou a partida final!")
        stop = True
    if ganha2 == 3:
        vencedor_partida = time_2
        print("O time " + vencedor_partida + " ganhou a partida final!")
        stop = True
    i = i + 1