'''
[LPIA-A01] Você está criando um programa para calcular a área de um retângulo. 
O programa deve solicitar ao usuário que forneça a base e a altura do retângulo. 
Em seguida, o programa deve calcular a área usando a fórmula:

Área=Base×Altura

O programa deve exibir a área calculada.

'''

base = float(input("Digite o valor da base do retângulo: "))
altura = float(input("Digite o valor da altura do retângulo: "))

area = base * altura

print(f"A área do retângulo é: {area:.2f}")