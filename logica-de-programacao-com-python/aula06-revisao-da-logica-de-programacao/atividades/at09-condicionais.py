'''
Categoria de Idade:
Desenvolva um programa que peça a idade do usuário e
informe se ele é criança, adolescente, adulto ou idoso.

'''

idade = int(input("Digite a sua idade: "))

if idade <= 12:
    categoria = "Criança"
elif 13 <= idade <= 17:
    categoria = "Adolescente"
elif 18 <= idade <= 59:
    categoria = "Adulto"
else:
    categoria = "Idoso"

print(f"\nVocê é classificado como: {categoria}")