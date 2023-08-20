estoque = 20
stop = False

while not stop:
    frase = str(input())
    if frase == 'Acabou uma partida e precisamos da seguinte quantidade de garrafas para matar a sede dos jogadores':
        qtd_jogadores = int(input())
        if qtd_jogadores > estoque:
            falta = qtd_jogadores - estoque
            print(f"Não teremos água para todos os jogadores... Temos que garantir {falta} garrafas!!")
            estoque = estoque * 2 - qtd_jogadores
            if estoque < 0:
                print("Por questões logísticas, teremos que acabar com os jogos..")
                stop = True
        else:
            estoque = estoque - qtd_jogadores
    elif frase == 'Encham o cooler! O jogo vai começar!!!!':
        estoque += 15
        print("Geladeira cheia!")
    elif frase == 'Timeout da partida! Verifiquem quantas garrafas pediram aos voluntários':
        quantidade_1 = int(input())
        quantidade_2 = int(input())
        quantidade_3 = int(input())
        quantidade_4 = int(input())
        quantidade_5 = int(input())
        estoque = estoque - quantidade_1 - quantidade_2 - quantidade_3 - quantidade_4 - quantidade_5
        if estoque < 0:
            estoque = estoque * -1
            print(f"Faltaram {estoque} garrafas para atender o pedido feito aos voluntários")
            print("Por questões logísticas, teremos que acabar com os jogos...") 
            stop = True
    elif frase == 'O InterCIn acabou!!! Vamos verificar nosso estoque de bebidas':
        stop = True
if estoque > 0:
    print(f"Sobraram {estoque} garrafas, vamos guardar na geladeira :D")
if estoque == 0:
    print("Vendemos todas as garrafas! Nosso planejamento foi perfeito!")