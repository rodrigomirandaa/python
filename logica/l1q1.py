#1) Faça um algoritmo que leia os valores A, B, C e imprima na tela se a soma de A + B é menor que C. 

def verifica_soma():

    A = int(input("Digite o valor de A: "))
    B = int(input("Digite o valor de B: "))
    C = int(input("Digite o valor de C: "))

    if A + B < C:
        print(f"A + B é: {A+B}, que é menor que: {C}")
    else:
        print(" A + B  é maior que C")


verifica_soma()

