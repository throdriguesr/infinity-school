'''
Objetivo: Peça ao usuário para digitar seu nome, idade e cidade
natal. Use uma f-string para formatar e exibir uma mensagem
com essas informações.

'''
nome = input("Qual seu nome? ")
idade = int(input("Qual sua idade? "))
cidade = input("Qual sua cidade natal? ")

print(f"\nSeu nome é {nome}, você tem {idade} anos e é natural de {cidade}. ")