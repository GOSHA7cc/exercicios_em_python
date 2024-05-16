# Escreva um programa que pergunte a quantidade de KM 
# percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro
# custa R$60 por dia e R$0,15 por KM rodado.

d = int(input("Quantos dias você alugou o carro? "))
km = float(input("Quantos KM você rodou com o carro? "))

d = 60 * d
km = 0.15 * km
t = d + km

print(f"Seu valor total ficou R${t:.2f}!") 