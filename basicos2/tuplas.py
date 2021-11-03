"""
Tuplas em python

Não é possível modificar uma tuplas, seu valor, seu índice
"""

tupla = (1, 2, 3, 'Julia', )

print(tupla[3])

for valor in tupla:
    print(valor)


print(tupla[1:])



print('#' * 40)
#######################################################################

#Criando tuplas
tupla1 = 1, 2, 3, 4, 5, 'baka', 'Fernando de noronha'

print(tupla1, type(tupla1))

tupla2 = 1, # Para criar uma tupla de um valor apenas, adicione ',' após o primeiro valor

print(tupla2, type(tupla1))


tupla3 = 1, 2, 3, 4, 5
tupla4 = 6, 7, 8, 9, 10

tupla5 = tupla3 + tupla4
print(tupla5)

#Desempacotamento de tuplas
v1, v2, v3, *_, v10  = tupla5

print(_)



#Convertendo tuplas em listas
tupla5 = list(tupla5)

print(tupla5)