# Escreva um programa que converta uma temperatura
# digitada em °C e converta para °F.

temp = float(input("Informe a temperatura em °C: "))
f = (temp * 1.8) + 32
# f = ((temp * 9) / 5) + 32

print(f"A temperatura de {temp:.1f}°C corresponde a {f:.1f}°F!")