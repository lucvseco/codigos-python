chance = int(input())


if chance <= 50:
    local_recomendado = str(input())
    print("Ufa, finalmente posso tirar minhas férias!")
    if local_recomendado == 'Maceió':
        print("Bem que eu tava com saudade de uma boa praia!")
    elif local_recomendado == 'Pipa':
        print("As noites em Pipa parecem muito animadas, to dentro!")
    elif local_recomendado == 'Caruaru':
        print("Parece um local muito divertido para aproveitar as festas juninas!")
    elif local_recomendado == 'Bonito':
        print("Praticar rapel nas cachoeiras vai ser demais!")
    else:
        frase = "Nunca ouvi falar sobre {}, mas me parece uma boa ideia!".format(local_recomendado)
        print(frase)

else:
    nome_do_heroi = str(input())
    print("Esses heróis nunca desistem, lá vou eu enfrentar mais um!")
    if nome_do_heroi == 'Homem-Aranha':
        print("O amigo da vizinhança nunca me deixa em paz! Será derrotado!")
    elif nome_do_heroi == 'Capitão América':
        print("Derrotar o carinha do escudo vai ser moleza!")
    elif nome_do_heroi == 'Spider Gwen':
        print("A namoradinha do spidey nunca será capaz de me derrotar!")
    elif nome_do_heroi == 'Hulk':
        print("Esse aí só sabe gritar e quebrar tudo, não será páreo para mim!")
    else:
        frase = "Não conheço esse herói {}. Preciso me preparar para essa batalha!".format(nome_do_heroi)
        print(frase)