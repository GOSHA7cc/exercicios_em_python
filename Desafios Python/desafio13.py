# Faça um algoritmo que leia o salário de um funcionário e mostre seu
# novo salário, com 15% de aumento.

n1 = float(input("Qual o seu salario? R$"))
aum = n1+(n1*0.15)

print(f"Seu novo salario é R${aum:.2f}!")