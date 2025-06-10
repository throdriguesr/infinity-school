'''
Atividade 04:
Verificação de Notas Aprovadas:
Escreva um programa que peça duas notas de um aluno. Use operadores
lógicos para verificar se as duas notas são maiores ou iguais a 6.

'''

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

if nota1 >= 6 and nota2 < 6:
    print(f"\nA primeira nota ({nota1}) é maior ou igual a 6, porém a segunda nota ({nota2}) não é.")

elif nota1 < 6 and nota2 >= 6:
    print(f"\nA primeira nota ({nota1}) não é maior ou igual a 6, porém a segunda nota ({nota2}) sim!")

elif nota1 >= 6 and nota2 >= 6:
    print(f"\nAs duas notas {nota1} e {nota2} são maiores ou iguais a 6.")

else:
    print(f"\nAs duas notas {nota1} e {nota2} são menores que 6.")