'''
Algoritmo de Cálculo de Desconto:
Crie um algoritmo que peça quatro notas de um aluno, calcule a
média e exiba se o aluno foi aprovado ou reprovado (média >= 6).

'''

notas = []

for i in range(1, 5):
    nota = float(input(f"Digite a nota {i}: "))
    notas.append(nota)

media = sum(notas) / len(notas)

situacao = "Aprovado" if media >= 6 else "Reprovado"

print(f"\nMédia: {media:.2f} - Situação: {situacao}")