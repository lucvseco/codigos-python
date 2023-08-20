n = int(input())
i = 0
nome_da_peca_indesejada1 = "colete preto"
nome_da_peca_indesejada2 = "coturno"
nome_da_peca_indesejada3 = "vestido com babados"
nome_da_peca_indesejada4 = "blusa bufante"
stop = False

while i < n and not stop:
    colecao = input()
    colecao_de_roupas = colecao.split(", ")

    if nome_da_peca_indesejada1 in colecao_de_roupas:
        print(f"{nome_da_peca_indesejada1} é uma peça muito gótica, não faz o estilo da Glimmer.")
        stop = True
    if nome_da_peca_indesejada2 in colecao_de_roupas and not stop:
        print(f"{nome_da_peca_indesejada2} é uma peça muito gótica, não faz o estilo da Glimmer.")
        stop = True
    if nome_da_peca_indesejada3 in colecao_de_roupas and not stop:
        print(f"{nome_da_peca_indesejada3} é uma peça muito antiquada, infelizmente essa coleção não vai servir...")
        stop = True
    if nome_da_peca_indesejada4 in colecao_de_roupas and not stop:
        print(f"{nome_da_peca_indesejada4} é uma peça muito antiquada, infelizmente essa coleção não vai servir...")
        stop = True
    notas = input()
    todas_as_notas = [int(nota) for nota in notas.split(', ')]
    media = int(sum(todas_as_notas)) / int(len(todas_as_notas))
    if media >= 6:
        print("Que coleção linda! Com certeza vai ajudar Glimmer a se inspirar.")
    else:
        print("Até que as peças são bonitinhas, mas não o bastante. Essa coleção não vai servir.")
    i += 1