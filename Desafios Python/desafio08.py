# Escreva um programa que leia um valor em metros e a exiba 
# convertido em centrímetros e milímetros.


n1 = float(input("Digite quantos metros você deseja converter: "))
c = n1 * 100
m = n1 * 1000

print("O seu valor em centimetros é {} e em milimetros é {}".format(c, m))