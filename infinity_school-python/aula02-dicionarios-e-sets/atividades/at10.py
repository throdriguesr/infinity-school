'''
Desenvolva um programa que recebe um dicionário, uma
chave e um valor como entrada e adiciona a chave e o
valor ao dicionário, atualizando o valor se a chave já existir.

'''

meu_dicionario = {"nome": "Thiago", "idade": 30, "cidade": "Belo Horizonte"}

print("\nDicionário atual:", meu_dicionario)

nova_chave = input("\nDigite a chave que deseja adicionar/atualizar: ")
novo_valor = input("Digite o valor para a chave: ")

meu_dicionario[nova_chave] = novo_valor

print("\n\nDicionário atualizado:", meu_dicionario)