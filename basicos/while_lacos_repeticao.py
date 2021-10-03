"""
while em python

utilizado para realizar ações enquanto
uma condição for verdadeira

Requisitos: entender condições e operadores
"""
nome = input('Digite o seu nome: ')

while nome != 'Juan':
    nome = input('Digite o seu nome: ')



x = 0
y = 0


"""
WHILE COM IF
"""

while x < 10:
    if x == 3:
        x = x + 1
        continue #Faz com o que o laço seja continuado
        # break faz com que o looping seja parado instantaneamente

    print(x)
    x = x + 1

print('Acabou ')

"""
WHILE COM HIERARQUIA
"""

while x < 10:
    y = 0
    while y < 5:
        print(f'X vale {x} e Y vale {y}')
        y += 1

    x += 1
print('Acabou o laço x')

"""
CALCULADORA
"""

while True:
    print()
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    operador = input('Digite um operador: ')
    sair = input('Deseja sair? [s]im ou [n]ão')

    if sair == 's':
        break

    if not num_1.isnumeric() or not num_2.isnumeric(): #Checa se só tem números 
        print('Você precisa digitar um número')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    # Operações: + , -, *, /

    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '*':
        print(num_1 * num_2)
    elif operador == '/':
        print(num_1 / num_2)
    else:
        print('Operador inválido')