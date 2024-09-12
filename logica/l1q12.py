#12) Escreva um algoritmo que leia o número de identificação, as 3 notas obtidas por um aluno nas 
#3 verificações e a média dos exercícios que fazem parte da avaliação, e calcule a média de 
#aproveitamento, usando a fórmula: 
#MA := (nota1 + nota 2 * 2 + nota 3 * 3 + ME)/7 
#A atribuição dos conceitos obedece a tabela abaixo. O algoritmo deve escrever o número do aluno, 
#suas notas, a média dos exercícios, a média de aproveitamento, o conceito correspondente e a 
#mensagem 'Aprovado' se o conceito for A, B ou C, e 'Reprovado' se o conceito for D ou E. 
#Média de aproveitamento Conceito 
#>= 90 A 
#>= 75 e < 90 B 
#>= 60 e < 75 C 
#>= 40 e < 60 D 
#< 40 E

def calcula_conceito():
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))

    MA = (nota1 + nota2*2 + nota3*3)/7

    if MA >= 90:
        print("Aprovado")
    elif MA >= 75 and MA < 90:
        print("Aprovado")
    elif MA >= 60 and MA < 75:
        print("Aprovado")
    elif MA >= 40 and MA < 60:
        print("Reprovado")
    elif MA < 40:
        print("Reprovado")

calcula_conceito()