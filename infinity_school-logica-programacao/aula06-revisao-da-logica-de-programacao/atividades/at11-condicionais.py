'''
Verificar Signo:
Escreva um programa que peça o dia e o mês de
nascimento do usuário e informe o signo correspondente.

'''

dia = int(input("Digite o dia do seu nascimento: "))
mes = int(input("Digite o mês do seu nascimento (1-12): "))

if (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
    signo = "Aquário"
elif (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
    signo = "Peixes"
elif (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
    signo = "Áries"
elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
    signo = "Touro"
elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
    signo = "Gêmeos"
elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
    signo = "Câncer"
elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
    signo = "Leão"
elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
    signo = "Virgem"
elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
    signo = "Libra"
elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
    signo = "Escorpião"
elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
    signo = "Sagitário"
elif (mes == 12 and dia >= 22) or (mes == 1 and dia <= 19):
    signo = "Capricórnio"
else:
    signo = "Data inválida"

print(f"\nSeu signo é: {signo}")