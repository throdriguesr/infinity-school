'''
Escreva um programa que percorra as chaves e valores 
de um dicionário separadamente e os exiba.

'''

dados = {
    'Nome': 'Thiago',
    'Idade': 30,
    'Cidade': 'Belo Horizonte'
}

print("Chaves do dicionário:")
for chave in dados.keys():
    print(chave)

print("\nValores do dicionário:")
for valor in dados.values():
    print(valor)