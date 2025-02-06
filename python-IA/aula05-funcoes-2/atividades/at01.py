'''
Crie um programa que solicita ao usuário que insira três notas e, em seguida, calcule a média dessas notas usando uma função. A função deve receber as três notas como argumentos e retornar a média. Por fim, o programa deve imprimir a média calculada.

'''

def calcular_media(n1, n2, n3):
    return (n1 + n2 + n3) / 3

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = calcular_media(nota1, nota2, nota3)

print(f"\nA média das notas é: {media:.2f}")