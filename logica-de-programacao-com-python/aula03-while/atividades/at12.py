'''
Senha correta: 
Desenvolva um programa que peça ao usuário para digitar uma
senha e continue pedindo até que a senha correta (previamente
definida) seja inserida.

'''

senha = input("Cadastre uma senha: ")

while True:
    senha2 = input("\nDigite a senha novamente: ")

    if senha2 == senha:
        print("\nSenha correta!")
        break

    else:
        print("\nSenha incorreta. Tente novamente")