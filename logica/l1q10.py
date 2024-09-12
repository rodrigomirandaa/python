#10) O IMC – Indice de Massa Corporal é um critério da Organização Mundial de Saúde para dar 
#umaindicação sobre a condição de peso de uma pessoa adulta. A fórmula é IMC = peso / ( altura )2  
#Elabore um algoritmo que leia o peso e a altura de um adulto e mostre sua condição de acordo 
#com a tabela abaixo.

def calcula_imc():
    peso = float(input("Digite o seu peso: "))
    altura = float(input("Digite a sua altura: Ex: 1.77 "))
    
    imc = peso / (altura**2)

    if imc < 18.5:
        print("Abaixo do peso, bora comer!")
    if imc >=18.5 and imc < 25:
        print("Normal..")
    if imc >=25 and imc < 30:
        print("Tá cheinho.. Fecha a boca!")
    if imc > 30:
        print("Bora procurar um nutri e fazer exercicio,passou da hora hein!")


calcula_imc()
