f1 = str(input())
funcionalidade_ponto1 = int(input())
f2 = str(input())
funcionalidade_ponto2 = int(input())
f3 = str(input())
funcionalidade_ponto3 = int(input())
f4 = str(input())
funcionalidade_ponto4 = int(input())
f5 = str(input())
funcionalidade_ponto5 = int(input())
ia = 'ativação de inteligência artificial'
visao = 'lentes de visão avançada'
lancador = 'novo lançador de teias'
balas = 'traje à prova de balas'
membrana = 'membranas palanadoras'
nada = 'NADA'
soma_funcionalidade = funcionalidade_ponto1 + funcionalidade_ponto2 + funcionalidade_ponto3 + funcionalidade_ponto4 + funcionalidade_ponto5

if f1 == lancador:
    if f2 == nada:
        if f3 == nada:
          if f4 == nada:
            if f5 == nada:
              frase_final = 'Aranha, nessa sequência você usou {} de energia!'.format(soma_funcionalidade)
              print(frase_final)
              exit() 
if f1 == lancador:
    print("Com calma, aranha")
    if f2 == visao:
        print("Lembre de desativar as lentes depois, e cuidado ao usar as teias no escuro")
elif f1 == lancador:
    print("Com calma, aranha")
    if f2 == visao:
        print("Lembre de desativar as lentes depois, e cuidado ao usar as teias no escuro")
        if f3 == balas:
            print("UOU, só tente sair dessa vivo, vou otimizar a energia aqui")
elif f1 == lancador:
    print("Com calma, aranha")
if f1 == ia or f2 == ia or f3 == ia or f4 == ia or f5 == ia:
    print("Espero que não esteja ativando isso para usar nas provas")
if 80 <= soma_funcionalidade:
    print("Vou descarregar em questão de minutos, pare AGORA")
if all(func in [f1, f2, f3, f4, f5] for func in [membrana, lancador, ia]):
    print("Tudo certo, mas cuidado ao ficar conversando com IA enquanto voa")


frase_final = 'Aranha, nessa sequência você usou {} de energia!'.format(soma_funcionalidade)
print(frase_final)