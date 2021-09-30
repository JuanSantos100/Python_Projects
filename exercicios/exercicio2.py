"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada.

0-11 bom dia, 12-17 boa tarde, 18-23 boa noite
"""
def configurandoHorario():
    horario = input('Digite um horário (0-23): ')
    if horario > 23:
        print('Favor, digitar um número entre 0-23')
    elif horario < 0:
        print('Favor, digitar um número entre 0-23')

    while horario.isdigit() == False:
        horario = input('Por favor, digite apenas números inteiros')
    horario = int(horario)

    if (horario >= 0 and horario <=11 ):
        print('Bom dia')

print()

