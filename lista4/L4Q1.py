def soma(x, y):
    resultado = x + y
    return resultado
def subtracao(x, y):
    resultado = x - y
    return resultado
def multiplicacao(x, y):
    resultado = x * y
    return resultado
def divisao(x, y):
    resultado = x / y
    return resultado
def potencia(x, y):
    resultado = x ** y
    return resultado
stop = False
n = int(input())
if n == 0:
  print("Vou relaxar aqui na minha nave")
  stop = True 
i = 1
while i <= n and not stop:
  frase = str(input())
  x = float(input())
  y = float(input())
  if frase == "Quero somar esses dois números:":
    resultado = soma(x, y)
  if frase == "Preciso subtrair um pelo outro":
    resultado = subtracao(x, y)
  if frase == "Quanto dá o produto disso?":
    resultado = multiplicacao(x, y)
  if frase == "Vou dividir aqui rapidinho":
    resultado = divisao(x, y)
  if frase == "E se eu elevar um pelo outro?":
    resultado = potencia(x, y)
  print(f"O resultado da {i}ª operação foi {resultado:.1f}")
  i += 1
if stop == False:
  print("Ufa, já deu de cálculos por hoje!")       