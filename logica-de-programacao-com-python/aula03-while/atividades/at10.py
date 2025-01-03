'''
Soma até 50: 
Escreva um programa que use um laço while para somar
números consecutivos começando de 1 e termine quando
a soma atingir ou ultrapassar 50.

'''

soma = 0
numero = 1

while True:
    soma += numero
    print(soma)
    if soma >= 50:
        break
    numero += 1

print(f"\nA soma dos números consecutivos é: {soma}")