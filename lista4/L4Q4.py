def checar_sobrevivencia(x_explosao, x_astronauta, y_explosao, y_astronauta, raio_impacto):
    sobreviventes = 0
    distancia = ((x_explosao - x_astronauta)**2 + (y_explosao - y_astronauta)**2 )**(1/2)
    if distancia >= raio_impacto:
        sobreviventes += 1
    return sobreviventes
def encontrar_pc(num_astronautas, x_total, y_total):
    media_x = x_total / num_astronautas
    media_y = y_total / num_astronautas
    pontoc = []
    pontoc.append(media_x)
    pontoc.append(media_y)
    return pontoc
def resgatar_astronautas(x_explosao, x_astronauta, y_explosao, y_astronauta, raio_impacto):
    n_sobreviventes = checar_sobrevivencia(x_explosao, x_astronauta, y_explosao, y_astronauta, raio_impacto)
    return n_sobreviventes

sobreviventes = 0
n_total = 0
lista_pc = []
entrada = input()
entrada1 = input()
raio_impacto = int(input())
capsulas = eval(entrada)
for sublist in capsulas[:]:
    if not sublist:
        capsulas.remove(sublist)
posicao_explosao = eval(entrada1)
x_explosao = int(posicao_explosao[0])
y_explosao = int(posicao_explosao[1])
for i, capsula in enumerate(capsulas):
    num_astronautas = 0
    x_total = 0
    y_total = 0
    i + 1
    for j, astronauta in enumerate(capsula):
        x_astronauta = astronauta[0]
        y_astronauta = astronauta[1]
        n = resgatar_astronautas(x_explosao, x_astronauta, y_explosao, y_astronauta, raio_impacto)
        if n == 1:
          num_astronautas += 1
          n_total += 1
          x_total += astronauta[0]
          y_total += astronauta[1]
        j + 1
    if num_astronautas != 0:
      pc = encontrar_pc(num_astronautas, x_total, y_total)
      lista_pc.append(pc)
print_lista = []
print_lista.append(n_total)
print_lista.append(lista_pc)
print(print_lista)