'''
Escreva um programa que recebe um dicionário e uma
lista de chaves como entrada e verifica se todas as
chaves da lista existem no dicionário. A função deve
retornar True se todas as chaves existirem e False caso contrário.

'''

dicionario = {'a': 1, 'b': 2, 'c': 3}
chaves = ['a', 'b']

resultado = True

for chave in chaves:
    if chave not in dicionario:
        resultado = False
        break

print(resultado)