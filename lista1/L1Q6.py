nome = str(input())
total_pessoas = int(input())
coef = float(input())

if coef % 2 == 0:
    res = coef * (total_pessoas - 1) + 1
else:
    res = coef * (total_pessoas - 1) / 2

parte_decimal = res - int(res)  

primeiro_digito_decimal = int(parte_decimal * 10)  

if primeiro_digito_decimal >= 1 and primeiro_digito_decimal <= 5:
    resultado_arredondado = int(res)  
elif primeiro_digito_decimal > 5 and primeiro_digito_decimal <= 9:
    resultado_arredondado = int(res) + 1 
else:
    resultado_arredondado = res  

proporcao = (resultado_arredondado * 100) / total_pessoas
proporcao_inteira = int(proporcao)

frase = "Vamos verificar se {} vai fumar singaro!".format(nome)
print(frase)
frase2 = "{}% dos seus amigos fumam singaro".format(proporcao_inteira)
print(frase2)
if proporcao_inteira < 25:
    print("Você tem poucas chances de fumar singaro, fuma não pow, cuide da sua saúde") 
elif 25 < proporcao_inteira < 50:
    print("Cuidado pra não fumar ein, fuma não pow, cuide da sua saúde")
elif 50 < proporcao_inteira:
    print("TIRA ESSE SINGARO DA BOCA. FUMA NÃO POW, CUIDE DA SUA SAÚDE!")



