#1) Desenvolver um algoritmo que efetue a soma de todos os números ímpares que são múltiplos de 
#três e que se encontram no conjunto dos números de 1 até 500. 

numero = 0
soma = 0

while numero < 500:
    numero = numero + 1

    if numero % 2 != 0 and numero % 3 == 0:
        soma = soma + numero

print(soma)

