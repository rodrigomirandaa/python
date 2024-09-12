#3) Faça um algoritmo para receber um número qualquer e informar na tela se é par ou ímpar. 

def verifica_par_impar():
    A = int(input("Digite um numero: "))

    if A%2 == 0:
        print(f"{A} é par")
    else: 
        print(f"{A} é impar")
        

verifica_par_impar()


