"""
Expressões Lambda - Python | Passando uma função para passar em outra função
Funções simples de pouco código
Funções anônimas

Não precisa de return
"""

def funcao(arg, arg2):
    return arg * arg2

var = funcao(2,2)
print(var)

#Experssão lambda
a = lambda x, y: x * y

print('Resultado Expressão lambda: {}'.format(a(2,2)))

print('#' * 40)
#######################################################################

#Sem usaar lambda
lista = [
    ['p1', 13],
    ['p2', 6],
    ['p3', 78],
    ['p4', 15],
    ['p5', 8],
]

#OBS: O INTERPRETADOR PYTHON NÃO SABE ORDENAR LISTAS DENTRO DE LISTAS

def func(item): #Função para retornar a chave do item que eu quero que ordene, neste caso, o preço do produto
    return item[1]

lista.sort(key=func, reverse=True) #Função sort para ordenar de acordo uma chave

print('Sem usar lambda: {}'.format(lista))

print('#' * 40)
#######################################################################

#Usando lambda
lista = [
    ['p1', 13],
    ['p2', 6],
    ['p3', 78],
    ['p4', 15],
    ['p5', 8],
]

lista.sort(key=lambda item: item[1]) #Função sort para ordenar de acordo uma chave

print('Usando lambda: {}'.format(lista))

print('#' * 40)
#######################################################################

#Usando SORTED +  Lambda
lista = [
    ['p1', 13],
    ['p2', 6],
    ['p3', 78],
    ['p4', 15],
    ['p5', 8],
]

print('Usando Sorted {}'.format(sorted(lista, key=lambda i: i[0], reverse=True)))