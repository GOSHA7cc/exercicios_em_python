# Faça um programa que leia a largura e a altura de uma parede em
# metros, calcule a sua área e a quantidade de tinta necessária para
# pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².


n1 = float(input("Qual a altura da sua parede? "))
n2 = float(input("Qual a largura da sua parede? "))
a = n1 * n2
t = a / 2

print("Você vai precisar de {:.1f} litros!".format(t))