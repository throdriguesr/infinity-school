'''
Algoritmo de Conversão de Tempo:
Desenvolva um algoritmo que converta uma quantidade de
segundos fornecida pelo usuário em horas, minutos e segundos.

'''

segundos_totais = int(input("Digite a quantidade de segundos: "))

horas = segundos_totais // 3600

minutos = (segundos_totais % 3600) // 60

segundos = segundos_totais % 60

print(f"\n{segundos_totais} segundos equivalem a {horas} horas, {minutos} minutos e {segundos} segundos.")