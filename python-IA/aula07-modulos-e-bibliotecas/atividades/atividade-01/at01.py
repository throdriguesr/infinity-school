'''
Crie um programa que será uma calculadora.
Nesta calculadora você deverá ter um módulo para as operações matemáticas, 
o arquivo principal deverá conter apenas um menu de escolha para o usuário 
(soma, subtração, multiplicação e divisão).

'''

# Aqui consta o ARQUIVO PRINCIPAL

import operacoes

def menu():
    while True:
        print("\nCalculadora:")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Sair")
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == '5':
            print("\nSaindo da calculadora...")
            break
        
        if opcao not in ['1', '2', '3', '4']:
            print("\nOpção inválida! Tente novamente.")
            continue

        try:
            num1 = float(input("\nDigite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("\nErro: Digite apenas números!")
            continue

        if opcao == '1':
            print(f"\nResultado: {operacoes.soma(num1, num2)}")
        elif opcao == '2':
            print(f"\nResultado: {operacoes.subtracao(num1, num2)}")
        elif opcao == '3':
            print(f"\nResultado: {operacoes.multiplicacao(num1, num2)}")
        elif opcao == '4':
            print(f"\nResultado: {operacoes.divisao(num1, num2)}")

        continuar = input("\nDeseja realizar outra operação? (Digite: sim ou não): ").strip().lower()
        if continuar != 'sim':
            print("\nObrigado por usar a calculadora. Até mais!")
            break

if __name__ == "__main__":
    menu()