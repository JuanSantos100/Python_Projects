lista = [0,1,2,3,4,5,6,7,8,9]

print(hasattr(lista, '__next__')) #hasattr verifica se uma variável tem uma determinada função


# for v in lista:
#     print(v)


lista2 = [0,1,2,3,4,5,6,7,8,9]
lista2 = iter(lista2)

print(next(lista2))


print('#' * 40, '\n')
###################################################
import sys
import time
lista3 = list(range(10000))

"""
Geradores podem servir para que nós não usemos memória demais para 
alocar dados grandes. Por ex.: uma lista com muitos valores
"""

print(sys.getsizeof(lista3)) # quantos bytes essa lista está consumindo de memória

print('#' * 40, '\n')
###################################################

print('Exemplificando geradores', '\n')

# def gera():
#     r = []
#     for n in range(100):
#         r.append(n)
#         time.sleep(0.1) #medido em segundos | simulação de algo pesado
#     return r

# g = gera()

# for v in g:
#     print(v)

print('#' * 40, '\n')
###################################################

print('Implementado geradores', '\n')

# def gerador():
#     for n in range(100):
#         yield n # retornando um valor de cada vez, ao invés de esperar por todos os valores
#         time.sleep(0.1)

# gerado = gerador()


# for v in gerado:
#     print(v)

print('#' * 40, '\n')
##################################################

"""
Listas = guardam todos os valores na memória e ocupam muito espaço no seu armazenamento

Geradores = guardam todos os valores da lista, porém só retorna um valor quando 
você solicitar por ele, através da função next() ou um laço for
"""

list1 = [x for x in range(100000)]
print(type(list1))
list2 = (x for x in range(100000)) #quando o list comprehension é feito com () se torna um generator
print(type(list2))

print(sys.getsizeof(list1))
print(sys.getsizeof(list2))