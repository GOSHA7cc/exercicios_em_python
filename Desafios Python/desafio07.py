# Desenvolva um programa que leia as duas notas de um aluno,
# calcule e mostre sua média.

a1 = float(input("Digite sua primeira nota: "))
a2 = float(input("Digite sua seginda nota: "))
s = a1 + a2
t = s / 2

print("A sua média é: {:.2f}".format(t))