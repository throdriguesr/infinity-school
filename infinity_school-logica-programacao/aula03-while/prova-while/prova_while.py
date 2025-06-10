'''
[LPIA-A03] Você está criando um programa em Python para simular um jogo simples de adivinhação. 
O programa deve ter um número fixo, por exemplo, 7, que o jogador deve adivinhar. 
O jogador terá até 3 tentativas para acertar o número.

Implemente o jogo utilizando um loop while para permitir que o jogador faça múltiplas tentativas 
até acertar ou atingir o limite de tentativas. 
Utilize a estrutura else para exibir uma mensagem de encorajamento caso o jogador acerte 
e uma mensagem de consolo caso as 3 tentativas se esgotem sem sucesso.

'''

numero = 7
tentativa = 1

while tentativa <= 3:

    palpite = int(input("\nDigite seu palpite: "))

    if palpite == numero:
        print("\nParabéns, você acertou!")
        break

    else:
        if tentativa >= 3:
            print("\nQue pena! Suas chances esgotaram.")
        
        else:
            print("\nTente novamente.")

    tentativa += 1

else: 
    print(f"\nO número secreto era {numero}. Tente novamente mais tarde!")