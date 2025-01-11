'''
[LPIA-A04] Você está desenvolvendo um programa em Python para calcular a soma dos números 
pares dentro de um intervalo determinado pelo usuário. 
O programa deve solicitar ao usuário que insira dois números inteiros, 
representando o início e o fim do intervalo (inclusive).

Utilize um loop 'for' para iterar sobre todos os números no intervalo e somar apenas os 
números pares. Implemente a estrutura 'else' para exibir uma mensagem indicando que não há 
números pares no intervalo, caso seja o caso.

Ao final, exiba a soma dos números pares encontrados.

'''

inicio = int(input("Digite o primeiro número: "))
fim = int(input("Digite o segundo número: "))
soma_pares = 0

for i in range (inicio,fim):

    if i % 2 == 0:
        soma_pares += i
    
else:
    if soma_pares == 0:
        print("Não há números pares no intervalo.")
        
    else:
        print(f"A soma dos números pares no intervalo é: {soma_pares}")