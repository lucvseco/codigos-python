nomeAranha1 = str(input())
ataqueAranha = int(input())
defesaAranha = int(input())
nomeAliado1 = str(input())
ataqueAliado = int(input())
defesaAliado = int(input())
nomeVilao1 = str(input())
ataqueVilao = int(input())
defesaVilao = int(input())
nomeCapanga1 = str(input())
ataqueCapanga = int(input())
defesaCapanga = int(input())
fatorSorte1 = int(input())
fatorSorte2 = int(input())
fatorSorte3 = int(input())
aranhaGanha = 0
vilaoGanha = 0
ganha = False 
print("1° confronto:")
if fatorSorte1 == 3:
        ataqueAranha1 = ataqueAranha + ataqueAliado
        defesaVilao1 = defesaVilao + defesaCapanga
elif fatorSorte1 == 1:
        ataqueAranha1 = ataqueAranha + ataqueAliado
        defesaVilao1 = defesaVilao
elif fatorSorte1 == 2:
        defesaVilao1 = defesaVilao + defesaCapanga
        ataqueAranha1 = ataqueAranha
elif fatorSorte1 == 0:
        ataqueAranha1 = ataqueAranha
        defesaVilao1 = defesaVilao
if ataqueAranha1 == defesaVilao1:
    if fatorSorte1 == 0 or fatorSorte1 == 3:
        aranhaGanha += 1
        ganha = True
    if fatorSorte1 == 1:
        aranhaGanha += 1
        ganha = True
    if fatorSorte1 == 2:
        vilaoGanha += 1
if ataqueAranha1 > defesaVilao1:
    aranhaGanha += 1
    ganha = True
if ataqueAranha1 < defesaVilao1:
    vilaoGanha += 1
if ganha == True:
    print("O " + nomeAranha1 + " acertou vários golpes no " + nomeVilao1)
else:
    print("O " + nomeVilao1 + " está dificultando a vida do " + nomeAranha1)

print("2° confronto:")
if fatorSorte2 == 3:
        ataqueVilao2 = ataqueVilao + ataqueCapanga
        defesaAranha2 = defesaAranha + defesaAliado
elif fatorSorte2 == 1:
       ataqueVilao2 = ataqueVilao + ataqueCapanga
       defesaAranha2 = defesaAranha
elif fatorSorte2 == 2:
        defesaAranha2 = defesaAranha + defesaAliado
        ataqueVilao2 = ataqueVilao
elif fatorSorte2 == 0:
        defesaAranha2 = defesaAranha
        ataqueVilao2 = ataqueVilao
if ataqueVilao2 == defesaAranha2:
    if fatorSorte2 == 0 or fatorSorte2 == 3:
        aranhaGanha += 1
        ganha = True
    if fatorSorte2 == 1:
        vilaoGanha += 1
    if fatorSorte2 == 2:
        aranhaGanha += 1
        ganha = True
if ataqueVilao2 > defesaAranha2:
    vilaoGanha += 1
if ataqueVilao2 < defesaAranha2:
    aranhaGanha += 1
    ganha = True
if ganha == True:
    print("O " + nomeAranha1 + " contra-atacou o " + nomeVilao1)
else:
    print("O " + nomeAranha1 + " não consegue se defender contra o " + nomeVilao1)

print("3° confronto:")
if fatorSorte3 == 3:
        ataqueAranha3 = ataqueAranha + ataqueAliado
        defesaVilao3 = defesaVilao + defesaCapanga
elif fatorSorte3 == 1:
        ataqueAranha3 = ataqueAranha + ataqueAliado
        defesaVilao3 = defesaVilao
elif fatorSorte3 == 2:
        defesaVilao3 = defesaVilao + defesaCapanga
        ataqueAranha3 = ataqueAranha
elif fatorSorte3 == 0:
        ataqueAranha3 = ataqueAranha
        defesaVilao3 = defesaVilao
if ataqueAranha3 == defesaVilao3:
    if fatorSorte3 == 0 or fatorSorte3 == 3:
        aranhaGanha += 1
        ganha = True
    if fatorSorte3 == 1:
        aranhaGanha += 1
        ganha = True
    if fatorSorte3 == 2:
        vilaoGanha += 1
if ataqueAranha3 > defesaVilao3:
    aranhaGanha += 1
    ganha = True
if ataqueAranha3 < defesaVilao3:
    vilaoGanha += 1
if ganha == True:
    print("O " + nomeAranha1 + " acertou vários golpes no " + nomeVilao1)
else:
    print("O " + nomeVilao1 + " está dificultando a vida do " + nomeAranha1)

if aranhaGanha > vilaoGanha:
     print("O " + nomeAranha1 + " e " + nomeAliado1 + " conseguiram derrotar o " + nomeVilao1 + " e recuperar o multiverso!")
else:
     print("O " + nomeVilao1 + " e " + nomeCapanga1 + " invadiram Nova York, onde estão os outros aranhas??")