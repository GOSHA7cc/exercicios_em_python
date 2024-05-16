# Crie um programa que leia quanto dinheiro uma pessoa tem na 
# carteira e mostre quantos Dólares ela pode comprar.

n1 = float(input("Quantos reais você tem? R$"))
d = n1 / 5.14

print("Você pode comprar US${:.2f} dólares".format(d))