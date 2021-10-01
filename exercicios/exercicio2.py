"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada.

0-11 bom dia, 12-17 boa tarde, 18-23 boa noite
"""
def configurandoHorario():
    horario = input('Digite um horario entre 0-23: ')
    horario = int(horario)
    if horario < 0 or horario > 23:
        print('Horário deve ser entre 0 e 23')

    else:
        if horario <= 11:
            print('Bom dia')
        elif horario <= 17:
            print('Boa tarde')
        else:
            print('Boa noite !!!')

configurandoHorario()
