#2) Desenvolver um algoritmo que leia a altura de 15 pessoas. Este programa deverá calcular e 
#mostrar : 
#. A menor altura do grupo; 
#b. A maior altura do grupo; 

cont=0
maior=0
menor=0

while cont < 15:
    altura = float(input(f"Digite a altura da pessoa {cont+1}: "))
    cont = cont + 1
    
    if altura > maior:
        maior = altura
    if altura < menor:
        menor = altura

print(f"A maior altura é: {maior}")
print(f"A menor altura é: {menor}")

