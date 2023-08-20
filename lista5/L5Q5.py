def castelo(mapa, sala_atual, espada, salas_visitadas):
    rupees = mapa[sala_atual].count('◇')
    if 'Zelda' in mapa[sala_atual]:
      if 'espada' in mapa[sala_atual]:
        if 'Agahnim' in mapa[sala_atual]:
            return 0, False
      else:
        return rupees, True
    total_rupees = rupees
    sucesso_resgate = False
    for porta in mapa[sala_atual]:
        if isinstance(porta, int) and porta not in salas_visitadas:
            nova_sala = porta
            salas_visitadas.add(nova_sala)
            total_rupees_nova_sala, sucesso_resgate_nova_sala = castelo(mapa, nova_sala, espada, salas_visitadas)
            total_rupees += total_rupees_nova_sala
            sucesso_resgate = sucesso_resgate or sucesso_resgate_nova_sala
    return total_rupees, sucesso_resgate
quantidade_salas = int(input())
mapa = []
for _ in range(quantidade_salas):
    elementos = input().split(" - ")
    sala = []
    for elemento in elementos:
        if elemento.isdigit():
            sala.append(int(elemento))
        else:
            sala.append(elemento)
    mapa.append(sala)
sala_inicial = int(input())
visita = {sala_inicial}
total_rupees, rescue_success = castelo(mapa, sala_inicial, False, visita)
if rescue_success:
    print(f"A princesa Zelda está a salvo e ainda conseguimos coletar {total_rupees} rupees")
else:
    print(f"Infelizmente a princesa ainda corre perigo, mas temos {total_rupees} rupees para nos ajudar nas buscas")