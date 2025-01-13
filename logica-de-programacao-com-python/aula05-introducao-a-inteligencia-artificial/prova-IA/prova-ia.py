'''
[LPIA-A05]Desenvolva um programa em Python para calcular a média de notas de alunos 
em uma disciplina. O programa deve solicitar ao usuário o número de alunos e, em seguida, 
para cada aluno, pedir o nome e três notas. 
Utilize um loop 'for' para iterar sobre os alunos e suas notas.

Além disso, implemente uma estrutura condicional para verificar se cada aluno foi aprovado 
ou reprovado, considerando que a média mínima para aprovação é 7.0. 
Exiba o nome do aluno, suas notas, média e a indicação de aprovação ou reprovação.

Ao final, exiba a média geral da turma.

'''

qt_alunos = int(input("Qual a quantidade de alunos? "))

soma_medias = 0

for i in range(qt_alunos):

    nome = input(f"\nDigite o nome do aluno {i+1}: ")
    nota1 = float(input(f"Digite a primeira nota de {nome}: "))
    nota2 = float(input(f"Digite a segunda nota de {nome}: "))
    nota3 = float(input(f"Digite a terceira nota de {nome}: "))

    media = (nota1 + nota2 + nota3) / 3

    if media >= 7.0:
        status = "Aprovado"

    else:
        status = "Reprovado"

    print(f"\nNome: {nome}")
    print(f"Notas: {nota1}, {nota2}, {nota3}")
    print(f"Média: {media:.2f}")
    print(f"Status: {status}\n")

    soma_medias += media

media_geral = soma_medias / qt_alunos

print(f"Média geral da turma: {media_geral:.2f}")