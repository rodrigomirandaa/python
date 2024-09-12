#6) Escreva um algoritmo que lê dois valores booleanos (lógicos) e então determina se ambos são 
#VERDADEIROS ou FALSOS. 

def booleano(): 
    A = int(input("Digite um valor lógico (booleano)"))

    if A == 1:
        print("Verdadeiro")
    elif A == 0: 
        print("Falso")
    else:
        print("Digite um booleano")


booleano()
