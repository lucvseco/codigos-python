def frase1 (v_qtd):
    v_qtd += 1
    return v_qtd
def frase2 (v_qtd):
    v_qtd -= 1
    return v_qtd
def calculo_velf (v_vel, v_qtd):
    z = v_vel * v_qtd
    return z
nome_participante, qtd_propulsores, velocidade_propulsor, veli, velf = [], [], [], [], []
stop = False
stop3 = True 
loops = 0
i = 0
desclassificados = 0
classificados = 0
while not stop:
    stop2 = False
    desclassificado = False
    entrada = input()
    if entrada == "FIM":
        stop = True
    else:
        valores = entrada.split()
        v_nome = valores[0]
        v_qtd = int(valores[1])
        v_vel = int(valores[2])
        vel = v_qtd * v_vel
        while not stop2:
            frase = str(input())
            if frase == "Um Droide apareceu do nada na pista, do nadaaa! Perdi o controle e bati em uma pedra.":
                v_qtd = frase2(v_qtd)
                if v_qtd == 0:
                    desclassificado = True
                    stop3 = True
                    stop2 = True
            if frase == "Opa esse participante tem ID de Droide, desclassificando em 3, 2, 1...":
                stop3 = False 
                stop2 = True
                desclassificado = True 
                desclassificados += 1
                print(f"O {v_nome} achou que não descobriríamos, tirem {v_nome} imediatamente da pista.")
            if frase == "Pit-Stop Espacial" and desclassificado == False:
                v_qtd = frase1(v_qtd)
            if frase == "Próximo" and desclassificado == False:
                stop2 = True
            if frase == "FIM":
                stop = True
                stop2 = True
        if desclassificado == True and stop3 == True:
            desclassificados += 1
            print(f"BUUMM!! Infelizmente, {v_nome} está fora da corrida.")
        if desclassificado == False: 
            classificados += 1
            z = calculo_velf(v_vel, v_qtd)
            qtd_propulsores.append(v_qtd)
            velf.append(z)
            nome_participante.append(v_nome)
            velocidade_propulsor.append(v_vel)
            veli.append(vel)
            print(f"--- Participante: {nome_participante[i]} ---")
            print(f"Qtd de propulsores Final: {qtd_propulsores[i]}")
            print(f"Velocidade Inicial: {veli[i]} km/h")
            print(f"Velocidade Final: {velf[i]} km/h")
            i+=1
        loops += 1
        l = loops - desclassificados
if classificados == 0:
    print("NÃO! Esses Droides me pagam, sabotaram minha corrida!")
else:
    print(f"Relatório da CIn Pod Race: {l} participantes terminaram a corrida e {desclassificados} foram desclassificados.")