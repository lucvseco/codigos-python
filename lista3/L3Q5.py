n = int(input())
num_linhas = n
num_colunas = n
matriz = []
for i in range(num_linhas):
    linha = []
    for j in range(num_colunas):
        entrada_valor = input()
        linha.append(int(entrada_valor))
    matriz.append(linha)
for linha in matriz:
    print(*linha)