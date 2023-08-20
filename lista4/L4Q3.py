def palindromo(input_str):
    input_str = str(input_str).replace(" ", "").lower()
    return input_str == input_str[::-1]

def distinto(input_str):
    input_str = input_str.replace(" ", "").lower()
    distinct = set(input_str)
    return len(distinct)
n = int(input())
for _ in range(n):
    entrada = input()
    if palindromo(entrada):
        if entrada.isnumeric():
            print(f'O número "{entrada}" é um palíndromo!')
            count = distinto(entrada)
            print(f'Há {count} número(s) distinto(s) na sequência de números.')
        else:
            print(f'A frase "{entrada}" é um palíndromo!')
            count = distinto(entrada)
            print(f'Há {count} letra(s) distinta(s) na frase.')
    else:
        print('A frase ou o número não é um palíndromo.')