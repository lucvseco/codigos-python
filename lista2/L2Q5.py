qtd_jogos = int(input())
i = 0
stop = False
pontuacao_totalM = 0
pontuacao_totalS = 0
 
while i < qtd_jogos and not stop:
    nome_time = str(input())
    gols = int(input())
    chutes = int(input())
    cartao_amarelo = int(input())
    cartao_vermelho = int(input())
    pontuacao = gols * 10 + chutes * 3 + cartao_amarelo * -2 + cartao_vermelho * -4
    if chutes * 0.3 <= gols :
        pontuacao += 3
    if cartao_amarelo <= cartao_vermelho:
        pontuacao -= 3
    if nome_time == 'Manchester CIn':
        pontuacao_totalM += pontuacao
        if pontuacao_totalM < 0:
            print("O time " + nome_time + " ficou com pontuação negativa. A aposta não é segura, podemos perder nosso dinheiro.")
            stop = True
    if nome_time == 'SpiCIn Girls':
        pontuacao_totalS += pontuacao
        if pontuacao_totalS < 0:
            print("O time " + nome_time + " ficou com pontuação negativa. A aposta não é segura, podemos perder nosso dinheiro.")
            stop = True
    i += 1

if pontuacao_totalS > pontuacao_totalM:
    soma = pontuacao_totalS + pontuacao_totalM
    porcentagem_time_vencedor = (pontuacao_totalS / soma) * 100
    nome_time_vencedor = "SpiCIn Girls"
else:
    soma = pontuacao_totalS + pontuacao_totalM
    porcentagem_time_vencedor = (pontuacao_totalM / soma) * 100
    nome_time_vencedor = "Manchester CIn"
if pontuacao_totalM > 0 or pontuacao_totalS > 0:
    print(f"Com {porcentagem_time_vencedor:.2f}% dos pontos, o time {nome_time_vencedor} pode garantir nosso dinheiro na CInBet, é uma das grandes apostas do InterCIn.")
