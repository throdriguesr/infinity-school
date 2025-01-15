'''
Sistema de Login com Tentativas Limitadas:
Desenvolva um programa que simule um sistema de login.
O programa deve solicitar o nome de usuário e senha até que o
usuário insira as credenciais corretas ou até que o número máximo
de tentativas seja atingido. Use um laço while com uma condicional
para verificar as credenciais e limitar as tentativas.

'''

usuario_cadastrado = "usuario123"
senha_cadastrada = "senha123"
tentativas = 0
max_tentativas = 3

while tentativas < max_tentativas:
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    if usuario == usuario_cadastrado and senha == senha_cadastrada:
        print("\nLogin bem-sucedido! Bem-vindo!")
        break
    else:
        tentativas += 1
        print(f"\nUsuário ou senha incorretos. Tentativas restantes: {max_tentativas - tentativas}")
else:
    print("\nNúmero máximo de tentativas atingido. Acesso bloqueado.")