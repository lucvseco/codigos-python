caracteristica1 = input()
caracteristica2 = input()
nome = input()
habilidade = input()
nota1 = int(input())
nota2 = int(input())
nota3 = int(input())
media = (nota1 + nota2 + nota3)/3

if caracteristica1 == 'Humildade' and caracteristica2 == 'Bondade':
    if nome == 'Mary' and nome == 'Ninguém':
        if habilidade == 'Dancar' or habilidade == 'Lancar':
            if 7 <= media:
               print("Siga em frente, olhe para o lado. Bem-vindo ao aranhaverso, Miranha Furacao!")
if caracteristica1 != 'Humildade' and caracteristica2 != 'Bondade':
    print("Ops, parece que não foi dessa vez, Miranha. Você terá que continuar na Carreta Furacao mesmo!")
    print("Infelizmente você não possui as característica necessárias!")
if nome != 'Mary':
    print("Ops, parece que não foi dessa vez, Miranha. Você terá que continuar na Carreta Furacao mesmo!")
    print("Infelizmente você não está apaixonado pela pessoa certa!")
if habilidade != 'Dancar' and habilidade != 'Lancar':
    print("Ops, parece que não foi dessa vez, Miranha. Você terá que continuar na Carreta Furacao mesmo!")
    print("Infelizmente você não possui as habilidades necessárias!")
if media < 7:
    print("Ops, parece que não foi dessa vez, Miranha. Você terá que continuar na Carreta Furacao mesmo!")
    print("Infelizmente você não obteve um bom desempenho escolar!")
