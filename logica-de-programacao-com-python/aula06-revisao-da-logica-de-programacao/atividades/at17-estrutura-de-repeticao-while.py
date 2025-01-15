'''
Verificação de Palíndromo:
Escreva um programa que solicite uma palavra ao usuário e
use um laço while para verificar se a palavra é um palíndromo
(lê-se da mesma forma de trás para frente).

'''

palavra = input("Digite uma palavra: ").lower()
inicio = 0
fim = len(palavra) - 1
e_palindromo = True

while inicio < fim:
    if palavra[inicio] != palavra[fim]:
        e_palindromo = False
        break
    inicio += 1
    fim -= 1

if e_palindromo:
    print(f"\nA palavra '{palavra}' é um palíndromo.")
else:
    print(f"\nA palavra '{palavra}' não é um palíndromo.")