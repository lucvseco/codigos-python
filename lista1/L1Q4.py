esconderijoVenom = input()
chances = 3
acertou = False

while chances > 0:
    possivel_local = input()

    if possivel_local.lower() == esconderijoVenom.lower():
        acertou = True
        break
    chances -= 1
    print("Carambolas, ele não está aqui. Ele continua se divertindo!")

if acertou:
    print("Ahá, te encontrei e é o fim das suas férias!")
else: 
    print("AAAAAAAH, ele escapou de vez!")