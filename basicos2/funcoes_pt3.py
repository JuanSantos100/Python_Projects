"""
Funcções (def) em Python - *args **kwargs Parte 3
"""

def func (*args):
    print(args) # Retorna uma tupla com os valores
    print(args[0])
    print(args[-1])
    print(len(args))


lista = [1,2,3,4,5]

print(*lista, sep='-') # desempacotando todos os valores de lista
func(1,2,3,4,5)


print('#' * 40)
####################################################

def tupla (*args):
    #args[0] = 15 a alteração em tuplas não é permitido
    print(args) # Retorna uma tupla com os valores

tupla(1,2,3,4,5,6,7,8,9)

print('#' * 40)
####################################################

def tupla_lista (*args):
    args = list(args) # Fazendo cast de uma tupla para lista
    args[0] = 15
    print(args) # Retorna uma tupla com os valores

tupla_lista(1,2,3,4,5,6,7,8,9)