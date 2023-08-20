stop = False
itens = input()
lista_de_itens = itens.split(", ")
numero_de_itens = len(lista_de_itens)

itens_casa = input()
lista_ia = itens_casa.split(", ")
numero_de_ia = len(lista_ia)

itens_comuns = [palavra for palavra in lista_de_itens if palavra in lista_ia]
numero_de_comuns = len(itens_comuns)
if numero_de_comuns == 0:
    print(f"Nossa, irei ao shopping agora mesmo! Não tenho nenhum dos {numero_de_itens} itens em casa.")
    stop = True
while not stop:
    print("Esses são os itens que já tenho em casa:")
    for i, palavra in enumerate(itens_comuns, start=1):
        print(f"{i}º item: {palavra}")
    if numero_de_comuns != 0:
        if numero_de_itens == numero_de_comuns:
            print(f"Que ótimo, consegui encontrar cada um dos {numero_de_itens} itens!")
            stop = True
        else:
            falta = numero_de_itens - numero_de_comuns
            print(f"Irei precisar comprar {falta} itens antes do meu encontro!")
            stop = True
print("Isso é tudo! Hora de me preparar!")