def contar_vogais_consoantes(codigo):
    vogais = 0
    consoantes = 0
    numeros_naturais = []
    codigo = codigo.lower()  # Converter todas as letras para minúsculas para contar corretamente
    for char in codigo:
        if char.isalpha():
            if char in 'aeiou':
                vogais += 1
            else:
                consoantes += 1
        elif char.isdigit():
            numeros_naturais.append(int(char))

    return vogais, consoantes, numeros_naturais

def verificar_sequencia_multiplos(numeros):
    if len(numeros) >= 2:
        primeiro_natural = numeros[0]
        sequencia_multiplos = all(num % primeiro_natural == 0 for num in numeros)
        return sequencia_multiplos
    return False

def calcular_posicao_eixo(codigo):
    vogais, consoantes, numeros_naturais = contar_vogais_consoantes(codigo)
    posicao_eixo = calcular_posicao_eixo_x(vogais, consoantes)

    if verificar_sequencia_multiplos(numeros_naturais):
        posicao_eixo = 3

    return posicao_eixo

def calcular_posicao_eixo_x(vogais, consoantes):
    if consoantes == 0:
        return 0
    resultado = vogais / consoantes
    resultado_piso = int(resultado)
    resto_divisao = resultado_piso % 7
    return resto_divisao

# Solicitar ao usuário que digite os códigos para os eixos X e Y
codigo_eixo_y = input()
codigo_eixo_x = input()

posicao_x = calcular_posicao_eixo(codigo_eixo_x)
posicao_y = calcular_posicao_eixo(codigo_eixo_y)

# Matriz original com a estrela na posição decifrada
matriz_com_estrela = []
for i in range(7):
    linha = ['.'] * 7
    if i == posicao_y:
        linha[posicao_x] = '☆'
    matriz_com_estrela.append(linha)

# Verificar se a estrela está na borda da matriz
if posicao_x in [0, 6] or posicao_y in [0, 6]:
    print("Ihhh, vou ter que relocalizar a câmera, uma fotografia com a estrela na borda não dá! Infelizmente demora um pouco para criar outro código...")
    print("Mesmo que eu não tenha conseguido uma matriz boa para tirar a foto, obrigado pelo seu tempo.")
elif posicao_x == 3 and posicao_y == 3:
    print("Ótimo, a estrela vai ficar exatamente no meio da fotografia! Posição melhor não existe!")
    print("Obrigado pela ajuda! A foto ficou ótima!")
else:
    print("Ok, agora é só enviar a matriz!")
    print("Obrigado pela ajuda! A foto ficou ótima!")
