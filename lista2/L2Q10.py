nome_aluno = str(input())
nome_professor = str(input())
stop = False
ponto_professor = 0
ponto_aluno = 0 
partidas_aluno = 0
partidas_professor = 0

print("E agora, só pela resenha:")
print("Melhor de 3 entre: " + nome_aluno + " e " + nome_professor + "!")
print("COMEÇOU!")

while not stop:
    num = int(input())
    if num % 2 == 0:
        ponto_professor += 1
    else:
        ponto_aluno += 1
    print(f"{ponto_aluno} - {ponto_professor}")
    if ponto_aluno - ponto_professor >= 2 and ponto_aluno >= 11:
        print(nome_aluno + " ganhou esta partida!")
        partidas_aluno += 1
        print("Placar: " + nome_aluno + " [" + str(partidas_aluno) + "-" + str(partidas_professor) + "] " + nome_professor)
        ponto_professor = 0
        ponto_aluno = 0 
    if ponto_professor - ponto_aluno >= 2 and ponto_professor >= 11:
        print(nome_professor + " ganhou esta partida!")
        partidas_professor += 1
        print("Placar: " + nome_aluno + " [" + str(partidas_aluno) + "-" + str(partidas_professor) + "] " + nome_professor)
        ponto_professor = 0
        ponto_aluno = 0 
    if partidas_professor == 2:
        print("FIM DA SÉRIE!")
        print(nome_professor + " ganhou a série! A experiência ganhou!")
        stop = True 
    if partidas_aluno == 2:
        print("FIM DA SÉRIE!")
        print(nome_aluno + " ganhou a série! Puro talento!")
        stop = True 