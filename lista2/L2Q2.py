participantes = int(input())
i = 0
maior_pontuacao = 0

while i < participantes:
    nome = str(input())
    pontuacao = int(input())
    penalidade = int(input())
    pontuacao_total = pontuacao - penalidade
    if pontuacao_total > maior_pontuacao:
        maior_pontuacao = pontuacao_total
        nome_maior = nome
    i += 1
print("O grande vencedor do torneio foi " + nome_maior + " com um total de " + str(maior_pontuacao) + " pontos!")


