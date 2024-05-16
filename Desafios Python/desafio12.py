# Faça um algoritmo que leia o preço de um produto e mostre o seu 
# novo preço, com 5% de desconto.


n1 = float(input("Qual o valor do produto? R$"))
desc = n1-(n1*0.05)

print(f"Seu desconto é de R${desc:.2f}!")