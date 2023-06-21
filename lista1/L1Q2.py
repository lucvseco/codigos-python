local = input()
ocorrencia = input()

if local == 'Queens' or local ==  'Times square' or local == 'Central Park':
    print("Parece que hoje teremos que dar umas teiada por aí... simboora!")
else:
    print("Tudo maravilindo! mas tenho que estudar para prova de Inglês e História ainda boy...")
if local == 'Queens':
    frase = "Eita... {}, e logo aqui perto da tia May viiu?!".format(ocorrencia)
    print(frase)
if local == 'Times square':
    frase = "Movimentação intensa de cria aqui pra variar, mas tem {}, não posso deixar isso acontecer!".format(ocorrencia)
    print(frase)
if local == 'Central Park':
    frase = "Nossa... {}, depois de salvar vou pegar um hot dog meermo.".format(ocorrencia)
    print(frase)