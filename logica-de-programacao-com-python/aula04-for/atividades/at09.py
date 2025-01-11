'''
Verificar Números Pares e Impares com Interrupção:
Crie um programa que use um laço for para contar de 1 a 20. Use condicionais para
identificar números pares e ímpares. Pare o loop ao encontrar o número 15, usando break.

'''

for numero in range(1, 21):
    if numero % 2 == 0:
        print(f"{numero} é par")
    else:
        print(f"{numero} é ímpar")
    
    if numero == 15:
        break