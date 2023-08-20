def fibonacci(n, a=0, b=1):
    if n == a or n == b:
        return True
    elif n < a:
        return False
    else:
        return fibonacci(n, b, a + b)

def output(vidas, casas, position=0):
    if position >= len(casas):
        print("Voce Adicionou A Master Sword ao seu inventario")
        print("Link Salve Hyrule!!!")
        return
    casa_atual = casas[position]
    if fibonacci(casa_atual):
        output(vidas, casas, position + 1)
    else:
        if vidas > 0:
            print("Oh nao, Link! Voce nao pode parar ainda, voce e a ultima esperança de Hyrule!")
            output(vidas - 1, casas, 0)
        else:
            print("A ultima defesa de Hyrule caiu, nao sobrou ninguem capaz de se opor a Ganondorf.")
vidas, quantidade_casas = map(int, input().split())
casas = []
i = 0
while i < quantidade_casas:
    casa = int(input())
    casas.append(casa)
    i+=1
output(vidas, casas)