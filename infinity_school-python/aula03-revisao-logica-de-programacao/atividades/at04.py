'''
Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25, 26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

'''

n = int(input("Quantas pessoas estão na turma? "))

if n <= 0:
    print("Número de pessoas inválido. O programa será encerrado.")
else:
    soma_idades = 0

    for i in range(n):
        idade = int(input(f"Digite a idade da {i + 1}ª pessoa: "))
        
        soma_idades += idade

    media_idade = soma_idades / n

    if 0 <= media_idade <= 25:
        print("A turma é jovem.")
    elif 26 <= media_idade <= 60:
        print("A turma é adulta.")
    elif media_idade > 60:
        print("A turma é idosa.")
    else:
        print("Erro: Idades inválidas.")