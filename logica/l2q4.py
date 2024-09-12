#4) Escrever um algoritmo que leia uma quantidade desconhecida de números e conte quantos deles 
#estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deve 
#terminar quando for lido um número negativo.

intervalo1 = 0
intervalo2 = 0
intervalo3 = 0
intervalo4 = 0

while True:
    numero = int(input("Digite um número (ou um número negativo para encerrar): "))
    if numero < 0:
        break

    if 0 <= numero <= 25:
        intervalo1 += 1
    elif 26 <= numero <= 50:
        intervalo2 += 1
    elif 51 <= numero <= 75:
        intervalo3 += 1
    elif 76 <= numero <= 100:
        intervalo4 += 1

print("Quantidade de números em cada intervalo:")
print(f"[0-25]: {intervalo1}")
print(f"[26-50]: {intervalo2}")
print(f"[51-75]: {intervalo3}")
print(f"[76-100]: {intervalo4}")
