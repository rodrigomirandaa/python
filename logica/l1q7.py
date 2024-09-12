#7) Faça um algoritmo que leia uma variável e some 5 caso seja par ou some 8 caso seja ímpar, 
#imprimir o resultado desta operação. 

def operacao_par_impar():
    A = int(input("Digite um numero: "))

    if A%2 == 0:
        print(f"Como {A} é par, temos que {A} + 5 é: {A+5}")
    else:
        print(f"Como {A} é impar, temos que {A} + 8 é: {A+8}")


operacao_par_impar()
