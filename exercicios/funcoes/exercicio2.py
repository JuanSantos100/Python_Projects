"""
Crie uma função que recebe 3 números como parâmetros e exiba a soma entre eles
"""

def soma_3_numeros (num1, num2, num3):
    resultado_da_soma = num1 + num2 + num3
    print(f'O resultado da soma é: {resultado_da_soma}')


primeiro = int(input('Digite o primeiro valor: '))
segundo = int(input('Digite o segundo valor: '))
terceiro = int(input('Digite o terceiro valor: '))
soma_3_numeros(primeiro, segundo, terceiro)