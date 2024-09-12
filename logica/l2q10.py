# 10) Escreva um algoritmo que leia um valor inicial A e imprima a sequência de valores do cálculo de 
# A! e o seu resultado. Ex: 5! = 5 X 4 X 3 X 2 X 1 = 120

A = int(input("Digite um valor inteiro positivo para calcular o fatorial: "))

if A < 0:
    print("O fatorial não está definido para números negativos.")
elif A == 0:
    print("0! = 1")
else:
    fatorial = 1
    sequencia = str(A)  # Começa a sequência com o valor inicial

    for i in range(A - 1, 0, -1):
        fatorial *= i
        sequencia += f" x {i}"  # Adiciona a próxima multiplicação na sequência

    sequencia += f" = {fatorial}"  # Adiciona o resultado final à sequência
    print(sequencia)
