'''
[LPIA-A06]  Crie um programa em Python que simule um sistema de login. 
O programa deve permitir ao usuário três tentativas para acertar o nome de usuário e a senha 
corretos. Caso o usuário erre as credenciais, o programa deve fornecer uma mensagem 
informando quantas tentativas restam. Se o usuário acertar, uma mensagem de boas-vindas 
deve ser exibida, e o programa deve terminar imediatamente.

Se todas as três tentativas falharem, o programa deve usar um loop for para exibir uma 
mensagem de "Acesso bloqueado" repetida três vezes.

'''
nome = input("Qual seu nome? ")
login_cadastro = input("Qual será seu login? ")
senha_cadastro = input("Qual será sua senha? ")
print("______________________________________________")

tentativa = 2

while tentativa >= 0:
    login_tentativa = input("\nDigite seu Login: ")
    senha_tentativa = input("Digite sua Senha: ")

    if login_tentativa == login_cadastro and senha_tentativa == senha_cadastro:
        print(f"\nOlá {nome}! Seja bem-vindo!")
        break
    
    else:
        print(f"\nCredenciais incorretas. Você ainda tem {tentativa} tentativa(s).")
        tentativa -= 1

    if tentativa < 0:
        print("\nVocê excedeu o número de tentativas.")
        for _ in range(3):
            print("Acesso bloqueado.")