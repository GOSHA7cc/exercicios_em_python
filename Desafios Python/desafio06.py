# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e
# raiz quadrada.

n = int(input("Digite um numero: "))
s1 = n * 2
s2 = n * 3
s3 = n ** (1/2)

print("O seu numero é {} o dobro dele é {} o triplo dele é {} e a raiz quadrada dele é {:.3f}".format(n, s1, s2, s3))
# outra forma de fazer como Gustavo Guanabara fez 
# print("O dobro de {} vale {}".format(n, (n*2)))
# print("O triplo de {} vale {} \nA raiz quadrada de {} é igual a {:.3f}".format(n, (n*3), n, (n**(1/2))))