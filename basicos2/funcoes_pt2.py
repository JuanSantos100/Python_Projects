"""
Funções (def) em Python - return - (Parte 2)
"""

def funcao(variavel):
    return variavel # A função irá retornar o resultado para uma variável qualquer que eu queira
    print('Isso não será executado') # Após o return, não é mais executado nenhuma linha de código

variavel = funcao('Valor que eu quero')
print(variavel) #resultado: none | None é um tipo de dado em python

if variavel:
    print(variavel)
else:
    print('nenhum valor')

print('#' * 40)
##########################################################

def divisao(num1, num2):
    if num2 == 0:
        return
    
    return num1 / num2

divide = divisao(8,0)
if divide: #If True
    print(divide)
else: #Else False
    print('Conta inválida !!!')

print('#' * 40)
##########################################################

def f(var):
    print(var)

def dumb():
    return f

var = dumb()
print(id(var), id(f))

if var == f:
    print('Var é igual a f')
else: 
    print('Blaaaaaa')

print('#' * 40)
##########################################################

def retornandoTuplas():
    return ('Luiz', 'John', 'Mateus') #Tuplas = listas que não podem ser alteradas

variavel = retornandoTuplas()
print(variavel, type(variavel))


