"""
Crie um programa que permita verifique o número inteiro, informando
se é ímpar, par e até mesmo se ele não digitou um número inteiro
"""

def parOuImpar():
    numero = input('Digite um numero: ')
    
    while numero.isdigit() == False: #isdigit() verifica se no texto tem apenas números
        numero = input('Opaaa, isso não é um número, digite apenas inteiros: ')
    
    numero = int(numero)
    if numero % 2 == 0:
        print(f'{numero} é par')
    else:
        print(f'{numero} é ímpar')
        

# numero = 2
# print(type(numero))
parOuImpar()


