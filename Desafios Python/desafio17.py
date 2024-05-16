# faça um programa que leia o comprimento do cateto oposto e do
# cateto adjacente de um triângulo retângulo, calcule e mostre
# o comprimento da hipotenusa.

# import math
from math import sqrt, hypot
co = float(input("Digite o valor do cateto oposto: "))
ca = float(input("Digite o valor do cateto adjacente: "))
h = sqrt(ca*ca + co*co) # math.sqrt
# h = (co ** 2 + ca ** 2) ** (1/2)
# h = hypot(co, ca) math.hypot

print(f"A hipotenusa vai medir: {h:.2f}") 