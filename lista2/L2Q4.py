n = int(input())
i = 0
maior_pontuacao = 0
menor_pontuacao = float('inf')

for i in range (n):
    nome_dupla = str(input())
    periodo_duplas = int(input())
    pontos_duplas = int(input())
    pontuacao_final = pontos_duplas / periodo_duplas
    if pontuacao_final > maior_pontuacao:
        maior_pontuacao = pontuacao_final
        dupla_vencedora = nome_dupla
    if pontuacao_final < menor_pontuacao:
        menor_pontuacao = pontuacao_final
        dupla_perdedora = nome_dupla
i += 1

print(f"A dupla vencedora foi {dupla_vencedora} com a pontuação final de {maior_pontuacao:.2f} pontos.")
print(f"A dupla perdedora foi {dupla_perdedora} com a pontuação final de {menor_pontuacao:.2f} pontos.")