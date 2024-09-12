#8) Escreva um algoritmo que leia três valores inteiros e diferentes e mostre-os em ordem 
#decrescente.  

def ordena_decrescente():

    A = int(input("Digite o numero A: "))
    B = int(input("Digite o numero B: "))
    C = int(input("Digite o numero C: "))

    numeros = [A,B,C]

    numeros.sort(reverse=True)

    print(f"Os numeros ordenados são: {numeros[0]}, {numeros[1]}, {numeros[2]}")

ordena_decrescente()

    
