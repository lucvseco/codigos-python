n = int(input())
criaturas = []
criaturas_repetidas = []
count = 1
j = 1

for _ in range(n):
    nome = input()

    if nome in criaturas:
        count += 1
    else:
        criaturas.append(nome)
if count != 1:
    while j < count:
        print("Criatura repetida")
        j += 1
print("Registradas:")
for criatura in criaturas:
    print(criatura)