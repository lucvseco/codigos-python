dados = []
n_famosos = int(input())
for i in range(n_famosos):
    entrada = input()
    partes = entrada.split(" - ")
    nome_famoso = partes[0]
    partes3 = partes[1].split()
    profissao, avaliacao_famoso, mes_planejado = partes3[0], partes3[1], partes3[2]
    dado = {
        "nome": nome_famoso,
        "profissao": profissao,
        "avaliacao": avaliacao_famoso,
        "mes": mes_planejado
    }
    dados.append(dado)
mes_consultado = int(input())
dados_marcados = []
for dado in dados:
    if dado['mes_planejado'] == mes_consultado and dado['avaliacao_famoso'] == "fake":
        dados_marcados.append(dado)

