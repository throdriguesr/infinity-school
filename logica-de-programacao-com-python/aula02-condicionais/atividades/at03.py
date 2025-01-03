'''
Atividade 03:
Verificação de Maioridade e Habilitação:
Crie um programa que peça a idade do usuário e se ele possui habilitação
(sim ou não). Use operadores lógicos para verificar se ele é maior de idade
(>= 18) e possui habilitação.

'''

idade = int(input("Digite a sua idade: "))
tem_habilitacao = input("Você possui habilitação? (sim ou não): ")

if idade >= 18 and tem_habilitacao == "sim":
    print("\nVocê é maior de idade e possui habilitação.")

elif idade >= 18 and tem_habilitacao == "não":
    print("\nVocê é maior de idade, mas não possui habilitação.")

elif idade < 18 and tem_habilitacao == "sim":
    print("\nVocê é menor de idade, mas possui habilitação.")

else:
    print("\nVocê é menor de idade e não possui habilitação.")