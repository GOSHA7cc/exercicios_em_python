# Faça um programa que leia um número inteiro e mostre na tela o seu
# sucessor e seu antecessor.

n = int(input("Digite um numero: "))
s1 = n - 1
s2 = n + 1

print("O valor antecessor é {} e o valor digitado é {} e o sucessor dele é {}".format(s1, n, s2))

# outra forma de fazer é 
# print("A analisando o valor {}, seu antecessor é {} e o sucessor é {}".format(n, (n-1), (n+1)))