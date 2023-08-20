estoque = 20
stop = False

while not stop:
    frase = str(input())
    #deposito
    if frase == 'Encham o cooler! O jogo vai começar!!!!':
        estoque += 15
        print("Geladeira cheia!")
    if frase == 'Timeout da partida, vamos ver quantas garrafas pediram a cada voluntário':
        quantidade_1 = int(input())
        quantidade_2 = int(input())
        quantidade_3 = int(input())
        quantidade_4 = int(input())
        quantidade_5 = int(input())
        estoque = estoque - quantidade_1 - quantidade_2 - quantidade_3 - quantidade_4 - quantidade_5
        if estoque < 0:
            total = estoque
            total = total * -1
            print(f"Prometemos distribuir {total} garrafas e zeramos")
            stop = True
    if frase == 'O InterCIn acabou!!! Vamos verificar nosso estoque de bebidas':
        stop = True
    if estoque < 0:
        n1 = estoque * -1
        print(f"Faltaram {n1} garrafas para atender o pedido feito aos voluntários")
        print("Por questões logísticas, teremos que acabar com os jogos...")
        stop = True
    
if estoque > 0:
    print(f"Sobraram {estoque} garrafas, vamos guardar na geladeira :D")
if estoque == 0:
    print("Vendemos todas as garrafas! Nosso planejamento foi perfeito!")
if estoque < 0:
    estoque = estoque * -1
    print(f"Estamos devendo {estoque} garrafas para os alunos...")