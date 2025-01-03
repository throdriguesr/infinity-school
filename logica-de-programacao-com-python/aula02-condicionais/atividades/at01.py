'''
Atividade 01:
Comparação de Idades:
Peça ao usuário duas idades e use operadores de comparação para
verificar se a primeira idade é maior, menor ou igual à segunda.

'''

idade1 = int(input("Digite a primeira idade: "))
idade2 = int(input("Digite a segunda idade: "))

if idade1 > idade2:
    print("\nA primeira idade é maior que a segunda.")

elif idade1 < idade2:
    print("\nA primeira idade é menor que a segunda.")
    
else:
    print("\nAs duas idades são iguais.")