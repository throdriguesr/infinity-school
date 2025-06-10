'''
Objetivo: Criar um Programa que Peça as 4 Notas Bimestrais e mostre a Média

'''
nota1 = float(input("Qual sua nota do primeiro bimestre? "))
nota2 = float(input("Qual sua nota do segundo bimestre? "))
nota3 = float(input("Qual sua nota do terceiro bimestre? "))
nota4 = float(input("Qual sua nota do quarto bimestre? "))

total = (nota1 + nota2 + nota3 + nota4) / 4

print(f"\nCom base nas suas notas, a média é: {total}")