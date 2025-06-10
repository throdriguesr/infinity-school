'''
Objetivo: Faça um programa que pergunte quanto você ganha por hora e o número de horas
trabalhadas no mês, calcule o salário total e exiba o resultado (Considere que você trabalha
20 dias no mês).

'''
salario = float(input("Qual o seu salário mensal? R$ "))
horas = float(input("Quantas horas você trabalhou essa semana? "))

horasTrabalhadas = horas * 4

print(f"\nVocê trabalhou {horasTrabalhadas} esse mês.")

salarioHora = salario / horasTrabalhadas

print(f"\nSeu salário por hora é: {salarioHora}")