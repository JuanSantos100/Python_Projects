"""
List Comprehension
"""

lista = [1,2,3,4,5,6,7,8,9]
lista2 = [variavel for variavel in lista]
print('Exemplo: ', lista2)

print('#' * 40, '\n')
#############################################################

ex2 = [v * 2 for v in lista]
print('Exemplo: ', ex2)

print('#' * 40, '\n')
#############################################################

ex3 = [(v1, v2) for v1 in lista for v2 in range(3)]
print('Exemplo 3: ', ex3)

print('#' * 40, '\n')
#############################################################


lista3 = ['Rebeca', 'Samuel', 'Lucas']
ex4 = [v.replace('a', '@') for v in lista3] #Substituindo valores por @
print('Exemplo 4: ', ex4) 


print('#' * 40, '\n')
#############################################################

tupla = (
    ('chave', 'valor'),
    ('chave2', 'valor2')
)

ex5 = [(valor, chave) for chave, valor in tupla] #Invertendo valores em tuplas
print('Exemplo 5: ', ex5)
ex5 = dict(ex5)
print(ex5)
print(ex5['valor2'])


print('#' * 40, '\n')
#############################################################

lista4 = list(range(100))
ex6 = [v for v in lista4 if v % 2 == 0 if v % 8 == 0] #Fazendo ifs
print('Exemplo 6: ', ex6)

ex7 = [valor if valor % 3 == 0 else '-'for valor in lista4] #Utilizando if else
print('Exemplo 7: ', ex7)

