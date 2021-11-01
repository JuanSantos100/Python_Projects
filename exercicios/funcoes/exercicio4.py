"""
Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne fizz, 
se o parâmetro da função for divisível por 5, retorne buzz. Se o parâmetro da 
função for divisível por 5 e por 3, retorne FizzBuzz, caso constrário, retorne número
inválido
"""

def FizzBuzz(valor):
    #Problema ao executar FizzBuzz
    # if valor % 3 == 0:
    #     if valor % 5 == 0:
    #         print('FizzBuzz')
    #     print('Fizz')
    # elif valor % 5 == 0:
    #     if valor % 3 == 0:
    #         print('FizzBuzz')
    #     print('Buzz')
    # else:
    #     print('Número inválido')

    #Solução curso
    if valor % 3 == 0 and valor % 5 == 0:
        return 'fizzbuzz'
    if valor % 3 == 0:
        return 'fizz'
    if valor % 5 == 0:
        return 'buzz'
    
    return f'Número inválo: {valor}'

numero = int(input('Digite um número: '))
print(FizzBuzz(numero))
