"""
Gerador de CPF matematicamente válido

"""

from random import randint
numero = str(randint(100000000, 999999999))

novo_cpf = numero
# print(novo_cpf)
reverse = 10
total = 0

"""
Ao total, serão necessárias 19 vezes para realizar
todos os cálculos
"""
for index in range(19): 
    #No íncide 8, retorna ele para 0 para prosseguir com a contagem a partir de 0
    if index > 8:
        index -= 9

    # print(novo_cpf[index])
    total += int(novo_cpf[index]) * reverse

    reverse -=1
    if reverse < 2:
        reverse = 11
        digito = 11 - (total % 11)

        if digito > 9: 
            digito = 0
        total = 0
        novo_cpf += str(digito)

print(novo_cpf)