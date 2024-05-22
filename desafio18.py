# Faça um programa que leia um ângulo qualquer
# e mostre na tela o valor do seno, cosseno e 
# tangente desse ângulo.

import math

a = float(input("Digite o ângulo desejado: "))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print(f"O ângulo de {a} tem o seno de {s:.2f} \nO ângulo de {a} tem o cosseno de {c:.2f}\nO ângulo de {a} tem a tangente de {t:.2f}")
