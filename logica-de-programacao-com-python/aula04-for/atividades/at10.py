'''
Contar Números Positivos e Negativos:
Peça ao usuário para inserir 10 números. Use um laço for com condicionais para contar quantos
são positivos e quantos são negativos. Pare o loop se o número 0 for inserido, usando break.

'''

positivos = 0
negativos = 0

for _ in range(10):
    numero = int(input("Digite um número: "))
    
    if numero == 0:
        break
    elif numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print(f"\nPositivos: {positivos}, Negativos: {negativos}")