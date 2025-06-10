'''
Crie uma função que receba um nome e imprima uma saudação personalizada.

'''

def saudacao(nome):
    print(f"\nOlá, {nome}! Seja bem-vindo!")

nome_usuario = input("Digite seu nome: ")

saudacao(nome_usuario)