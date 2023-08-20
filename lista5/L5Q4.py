def derivada(coef, order, novo_coef=None):
    if novo_coef is None:
        novo_coef = [0] * len(coef)
    if order == 0:
        return novo_coef
    for i in range(1, len(coef)):
        novo_coef[i - 1] = i * coef[i]
    return derivada(novo_coef, order - 1, novo_coef)

def polinomio(coef):
    termos = []
    for i, coef in enumerate(coef):
        if coef != 0:
            if i == 0:
                termo = str(coef)
            elif i == 1:
                if coef == 1:
                    termo = "x"
                elif coef == -1:
                    termo = "-x"
                else:
                    termo = f"{coef}x"
            else:
                if coef == 1:
                    termo = f"x^{i}"
                elif coef == -1:
                    termo = f"-x^{i}"
                else:
                    termo = f"{coef}x^{i}"
            termos.append(termo)
    return "+".join(termos)
G = int(input())
K = int(input())
Q = int(input())
coef = [0] * (G + 1)
for _ in range(Q):
    linha = input().split(":")
    E = int(linha[0].split()[-1])
    C = int(linha[1])
    coef[E] = C
p1 = polinomio(coef)
derivadap1 = derivada(coef, K)
p2 = polinomio(derivadap1)
if p1 == "":
    p1 = "0"
if p2 == "":
    p2 = "0"
p1 = p1.replace("+-", "-")
p2 = p2.replace("+-", "-")
print(f"A derivada {K} do polinômio {p1} é")
print(f"{p2}")