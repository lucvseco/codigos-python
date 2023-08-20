equipe1_nome1 = str(input())
equipe1_nome2 = str(input())
equipe2_nome1 = str(input())
equipe2_nome2 = str(input())
i = 0
stop = False
pontos_totais_dupla1 = 0
pontos_totais_dupla2 = 0
vitorias_dupla1 = 0
vitorias_dupla2 = 0
quantidade_partidas = int(input())
print(f"VAMO VER QUEM VAI COMER GRAMA! TEREMOS {quantidade_partidas} PARTIDAS ENTRE:")
print(equipe1_nome1 + " e " + equipe1_nome2 + " X " + equipe2_nome1 + " e " + equipe2_nome2)

while i < quantidade_partidas:
    qtd_pontos1 = int(input())
    qtd_pontos2 = int(input())
    if qtd_pontos1 == 0 and not stop:
        print("JOGO ENCERRADO POR DESISTÊNCIA DA EQUIPE 1, QUE VERGONHA")
        stop = True 
    if qtd_pontos2 == 0 and not stop:
        print("JOGO ENCERRADO POR DESISTÊNCIA DA EQUIPE 2, QUE VERGONHA")
        stop = True 
    if qtd_pontos1 > qtd_pontos2:
        vitorias_dupla1 += 1
    elif qtd_pontos1 < qtd_pontos2:
        vitorias_dupla2 += 1   
    else:
        vitorias_dupla1 += 1   
    pontos_totais_dupla1 += qtd_pontos1
    pontos_totais_dupla2 += qtd_pontos2
    pontuacao_final1 = pontos_totais_dupla1 * (vitorias_dupla1/quantidade_partidas)
    pontuacao_final2 = pontos_totais_dupla2 * (vitorias_dupla2/quantidade_partidas)
    pontos_totais_da_disputa = pontos_totais_dupla1 + pontos_totais_dupla2
    i += 1
if pontuacao_final1 > pontuacao_final2:
    nome_vencedor1 = equipe1_nome1
    nome_vencedor2 = equipe1_nome2
    quantidade_de_vitorias = vitorias_dupla1
    quantidade_total_de_pontos_da_dupla = pontos_totais_dupla1
elif pontuacao_final1 < pontuacao_final2:
    nome_vencedor1 = equipe2_nome1
    nome_vencedor2 = equipe2_nome2
    quantidade_de_vitorias = vitorias_dupla2
    quantidade_total_de_pontos_da_dupla = pontos_totais_dupla2
else:
    nome_vencedor1 = equipe1_nome1
    nome_vencedor2 = equipe1_nome2
    quantidade_de_vitorias = vitorias_dupla1
    quantidade_total_de_pontos_da_dupla = pontos_totais_dupla1
print(f"CARAMBA! Tivemos um total de {pontos_totais_da_disputa} bolas ao chão ao longo dessa disputa.")
print(nome_vencedor1 + " e " + nome_vencedor2 + " são os grandes vencedores!")
print(f"Mataram {quantidade_total_de_pontos_da_dupla} bolas, ganhando {quantidade_de_vitorias} partidas")