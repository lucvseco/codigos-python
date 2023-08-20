def suspeito(nome_suspeito, string_concat):
    def minuscula(s):
        return s.lower()
    minuscula_suspeito = minuscula(nome_suspeito)
    minuscula_concatenated = minuscula(string_concat)
    def recursao(suspeito, concat_str, posicao):
        if len(suspeito) == 0:
            return True
        if posicao >= len(concat_str):
            return False
        if concat_str[posicao:].startswith(suspeito):
            return True
        return recursao(suspeito, concat_str, posicao + 1)
    return recursao(minuscula_suspeito, minuscula_concatenated, 0)
nome_suspeito = input()
string_concat = input()
if suspeito(nome_suspeito, string_concat):
    print(f"Encontrei, o culpado é o {nome_suspeito}!")
else:
    print(f"Infelizmente, {nome_suspeito} não é o culpado. A busca continua.")