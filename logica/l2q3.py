#3) Desenvolver um algoritmo que leia um número não determinado de valores e calcule e escreva a 
#média aritmética dos valores lidos, a quantidade de valores positivos, a quantidade de valores 
#negativos e o percentual de valores negativos e positivos. 

soma = 0
cont = 0
positivos = 0
negativos = 0

while True:
    valor = float(input("Digite o valor: ")) 
    if valor == 0:
        break

    soma = soma + valor
    cont = cont + 1

    if valor > 0:
        positivos = positivos + 1
    else:
        negativos = negativos + 1

if cont  > 0:
    media = soma / cont
    perc_positivos = (positivos / cont) * 100
    perc_negativos = (negativos / cont) * 100

    print(f"Média aritmética dos valores: {media:.2f}")
    print(f"Quantidade de valores positivos: {positivos}")
    print(f"Quantidade de valores negativos: {negativos}")
    print(f"Percentual de valores positivos: {perc_positivos:.2f}%")
    print(f"Percentual de valores negativos: {perc_negativos:.2f}%")
else:
    print("Nenhum valor foi digitado.")

        