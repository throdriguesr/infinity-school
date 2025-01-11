'''
Cálculo de Média de Notas:
Escreva um programa que solicite 5 notas de alunos. Use um laço for
para somar as notas e uma condicional para exibir a média e a
classificação ("Aprovado" para média >= 6, "Reprovado" para média < 6).

'''

soma_notas = 0

for _ in range(5):
    nota = float(input("Digite uma nota: "))
    soma_notas += nota

media = soma_notas / 5
classificacao = "Aprovado" if media >= 6 else "Reprovado"

print(f"\nMédia: {media:.2f}")
print(f"\nClassificação: {classificacao}")