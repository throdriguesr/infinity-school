'''
Crie uma função que receba um horário e imprima "Bom dia!", "Boa tarde!" ou "Boa noite!" conforme o horário.

'''

def saudacao_por_horario(horario):
    hora, minuto = map(int, horario.split(":"))
    
    if 6 <= hora < 12:
        print("\nBom dia!")
    elif 12 <= hora < 18:
        print("\nBoa tarde!")
    elif 18 <= hora < 24 or 0 <= hora < 6:
        print("\nBoa noite!")
    else:
        print("\nHorário inválido!")

horario_usuario = input("Digite o horário (no formato HH:MM): ")

saudacao_por_horario(horario_usuario)