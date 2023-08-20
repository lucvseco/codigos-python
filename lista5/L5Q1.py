def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

def decifrar(enigma):
    minusculas = 0
    maiusculas = 0
    for char in enigma:
        if char.islower():
            minusculas += 1
        elif char.isupper():
            maiusculas += 1
    total = len(enigma)
    if minusculas > maiusculas:
        k = minusculas
    else:
        k = maiusculas
    if minusculas != maiusculas:
        preco = fatorial(k) * total
    else:
        preco = total ** 2
    return preco
enigma_string = input()
preco = decifrar(enigma_string)
if preco >= 100:
    print(f"Hum... {preco}? Acho que na volta eu compro")
else:
    print(f"{preco}! Vou comprar todos!")