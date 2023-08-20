stop = False
i = 0
while not stop:
    entrada1 = str(input())
    if entrada1 == "Explorar arara":
        profissoes = input()
        lista_de_profissoes = profissoes.split(", ")
        quantidade1 = len(lista_de_profissoes)
        profissoes2 = input()
        lista_de_profissoes2 = profissoes2.split(", ")
        quantidade2 = len(lista_de_profissoes2)
        set1 = set(lista_de_profissoes)
        set2 = set(lista_de_profissoes2)
    elif entrada1 == "Meninas, acho que já falei demais. Vamos para o shopping?":
        stop = True
    if stop == False:
        print(f"Arara {i}:")
        if quantidade1 != quantidade2:
            print("Hmm, estranho! Acho que a Barbie se confundiu na organização e nas lembranças!")
        if set1 == set2:
            print("Boa, Barbie! Não bagunçou nada, pode contar todas as suas histórias!")
        elif quantidade1 == quantidade2:
            profissoes_dif = [elemento for elemento in lista_de_profissoes if elemento not in set1]
            total_nao_encontrados = len(profissoes_dif)
            print(f"Poxa, Barbie! Você acabou desorganizando essa arara, e {total_nao_encontrados} profissões vão ficar de fora da conversa. São elas: {profissoes_dif}.")
    i += 1

