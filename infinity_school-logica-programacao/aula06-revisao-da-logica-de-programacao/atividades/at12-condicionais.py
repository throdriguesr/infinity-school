'''
Sistema de Login:
Desenvolva um programa que simule um sistema de login.
O programa deve pedir o nome de usuário e a senha e verificar
se correspondem a um usuário pré-cadastrado. Exiba mensagens
apropriadas para login bem-sucedido ou falha.

'''

usuario_cadastrado = "usuario123"
senha_cadastrada = "senha123"

usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

if usuario == usuario_cadastrado and senha == senha_cadastrada:
    print("\nLogin bem-sucedido! Bem-vindo!")
else:
    print("\nFalha no login! Usuário ou senha incorretos.")