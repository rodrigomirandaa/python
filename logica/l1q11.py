#11) Elabore um algoritmo que calcule o que deve ser pago por um produto, considerando o preço 
#normal deetiqueta e a escolha da condição de pagamento. Utilize os códigos da tabela a seguir 
#para ler qual acondição de pagamento escolhida e efetuar o cálculo adequado. 
#Código Condição de pagamento 
#1 À vista em dinheiro ou cheque, recebe 10% de desconto 
#2 À vista no cartão de crédito, recebe 15% de desconto 
#3 Em duas vezes, preço normal de etiqueta sem juros 
#4 Em duas vezes, preço normal de etiqueta mais juros de 10%


def calcula_preco():
    
    valor_produto = float(input("Digite o valor do produto. Ex: 4.99:  "))
    forma_pgto = int(input("Digite a forma de pagamento, sendo 1 - Á vista, 2- Á vista(cartão), 3- 2x no cartão, 4- 3x no cartão:  "))

    if forma_pgto == 1:
        print(f"O valor final é: {valor_produto*0.9}")
    elif forma_pgto == 2:
        print(f"O valor final é {valor_produto*0.85}")
    elif forma_pgto == 3:
        print(f"O valor final é: {valor_produto}")
    elif forma_pgto == 4:
        print(f"O valor final é: {valor_produto*1.2}")
    else:
        print("Digite uma forma de pagamento válida")
calcula_preco()