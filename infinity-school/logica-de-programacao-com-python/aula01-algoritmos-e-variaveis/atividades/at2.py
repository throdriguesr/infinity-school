'''
Atividade 02: Crie um programa que peça ao usuário para digitar:
1.Seu nome;
2.Sua idade;
3.Sua altura;
4.Em seguida, imprima esses valores e seus respectivos tipos.

'''
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura (em metros): "))

print("\nDados fornecidos:")
print(f"Nome: {nome} (tipo: {type(nome)})")
print(f"Idade: {idade} (tipo: {type(idade)})")
print(f"Altura: {altura} (tipo: {type(altura)})")