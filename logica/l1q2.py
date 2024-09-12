#2) Faça um algoritmo que leia o nome, o sexo e o estado civil de uma pessoa. Caso sexo seja “F” e
#estado civil seja “CASADA”, solicitar o tempo de casada (anos). 

def verifica_casamento():
    nome = input("Digite o nome: ")
    sexo = input("Digite o sexo: ")
    estado_civil = input("Digite o estado civil: ")

    if sexo == "F" and estado_civil == "casada":
        tempo_casamento = int(input("Digite o tempo de casamento: "))


verifica_casamento()


        
