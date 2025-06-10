'''
Desenvolva um jogo de adivinhação em que o programa escolhe um número aleatório e desafia o jogador a adivinhá-lo. 
Forneça dicas ao jogador, indicando se o número é maior ou menor do que a adivinhação atual.

'''

import random

numero_secreto = random.randint(1, 100)

print("Bem-vindo ao Jogo de Adivinhação!")
print("Tente adivinhar o número entre 1 e 100.")

while True:
    try:
        palpite = int(input("\nDigite seu palpite: "))

        if palpite == numero_secreto:
            print("\nParabéns! Você acertou o número!")
            break

        elif palpite < numero_secreto:
            print("\nO número secreto é maior!")

        else:
            print("\nO número secreto é menor!")

    except ValueError:
        print("\nDigite um número válido!")