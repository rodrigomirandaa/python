#5) Encontrar o dobro de um número caso ele seja positivo e o seu triplo caso seja negativo,
#imprimindo o resultado

def dobro_triplo():
    A = int(input("Digite um numero: "))

    if A<0:
        print(f"O triplo de {A} é: {A*3}")
    else:
        print(f"O dobro de {A} é: {A*2}")


dobro_triplo()

