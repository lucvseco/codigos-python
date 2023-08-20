n = int(input())

a, b = 0, 1

print("A sequência de número das camisas do seu time será:", end=" ")
if n >= 1:
    print(b, end=" ")

for i in range(1, n):
    prox_n = a + b
    print(prox_n, end=" ")
    a, b = b, prox_n