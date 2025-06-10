'''
Escreva um programa que EXIBA um dicionário contendo
informações de pessoas (nome, idade) e exiba essas informações.

'''

pessoas = {
    "Pessoa1": {"nome": "Thiago", "idade": 30},
    "Pessoa2": {"nome": "Helena", "idade": 25},
    "Pessoa3": {"nome": "Altino", "idade": 60}
}

print("Informações das pessoas:")
for chave, valor in pessoas.items():
    print(f"{chave} - Nome: {valor['nome']}, Idade: {valor['idade']}")