#9) Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que 
#calcule seu peso ideal, utilizando as seguintes fórmulas: 
#para homens: (72.7 * h) – 58; 
#para mulheres: (62.1 * h) – 44.7. 

def calcula_peso_ideal():

    altura = float(input("Digite sua altura: "))
    sexo = input("Digite o seu sexo (M ou F): ")

    if sexo == "M":
        print(f"Seu peso ideal é: {72.7*altura}")
    elif sexo == "F":
        print(f"Seu peso ideal é {62.1*altura}")
    else:
        print("Digite um sexo válido")

calcula_peso_ideal()



 