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

    for valores in args:
        print(valores)

    # print(args) # Retorna uma tupla com os valores

tupla_lista(1,2,3,4,5,6,7,8,9)

print('#' * 40)
####################################################

def tupla_lista_2 (*args):
    print(args)

lista = [1,2,3,4,5]
tupla_lista_2(lista)
lista2 = [10,20,30,40,50]
tupla_lista_2(*lista, *lista2) #Enviando a lista desenpacotada || Isso faz com que os itens da minhas lista sejam parte da minha tupla

print('#' * 100)
print('\n KWARGS \n')
####################################################

def kwargs (*args, **kwargs): #args e kwargs é puramente convenção da comunidade python
    print(args)
    print(kwargs) #Exibição feita em modo de dicionário
    print(kwargs['nome']) #Acessando o valor do parâmetro nomeado

    nome = kwargs.get('nome')#outra forma de acessar o parâmetro nomeado |  MUITO MELHOR
    print(nome)

    idade = kwargs.get('idade') #caso o parâmetro não foi informado, irá retornar None
    if idade is not None:
        print(f'Idade: {idade}')
    else:
        print('Idade não informada')

ex_args = [1,2,3,4,5]
ex_args2 = [10,20,30,40,50]
kwargs(*ex_args, *ex_args2, nome='Julia', sobrenome='Vitória', idade = 45) # os parâmetros nomeados não serão exibidos no *args, apenas no **kwargs