n = str(input("Qual o seu nome? "))

print(f"Olá, {n}! \n Seja muito bem vindo!")

dia = int(input("Qual dia você nasceu ? "))
mes = str(input("Qual mes você nasceu ? "))
ano = int(input("Qual o ano que você nasceu ? "))


if ano >= 2006: 
    print("Você não pode alugar um carro!")
    
else:
    print(f"Você nasceu em {dia} de {mes} de {ano}!")

day = int(input("Quantos dias você rodou com o carro? "))
km = float(input("Quantos KM você rodou com o carro ? "))

day = 100 * day
km = 10 * km
tdk = day + km

print(f"Total a pagar {tdk}! \nObrigado pela preferencia!")
