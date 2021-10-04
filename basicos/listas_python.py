"""
Listas em Python
 Fatiamento
 append, insert, pop, del, clear, extend, + 
 min, mas 
 range
"""
#         0    1    2    3    4    5
lista = ['A', 'B', 'C', 'D', 'E', 10.5]

#print(lista[::-1])

l1 = [1,2,3]
l2 = [4,5,6]
l3 = l1 + l2

#print(l3)

l1.extend(l2)  #faz a extensão da lista com valores, nesse caso, adicionou toda a lista 2
# print(l1)
# print(l2)

l2.append('b') #adiciona um valor ao fim da lista
print(l2)