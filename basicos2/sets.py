"""
add (adiciona), update (atualiza), clear, discard
union | (une)
intersection & (todos os elementos presentes nos dois sets)
difference - (elementos apenas no set da esquerda)
symmetric_difference ^ (Elementos que estão nos dois sets, mas não em ambos)
"""

# Sets não possuem índices
set1 = {1,2,3,4,5,6,7,8,9} # Sets, só recebem valores, e nao par chave_valor
# print(set1)

for valor in set1:
    print(valor)

#para criar um set vazio, use set()
set2 = set()
set2.add(1)
set2.add(2)
set2.add(3)
set2.add('João')
set2.add((1,2,3,4))
set2.update('Python') #Essta função recebe um iterável como parâmetro, ou seja, será adicionado no set() cada uma das letras da palavra: Python
set2.update([1,2,3,4,5], {5,6,7,8}) #Essta função recebe um iterável como parâmetro, ou seja, será adicionado no set() cada uma das letras da palavra: Python


#Sets não aceitam elementos duplicados

print(f'Set2: {set2}')


# retirando valores do set
set2.discard(1)
print(f'Set2: {set2}')


print('#'*40, '\n')
#########################################################################
lista = [1,2,3,4,5,5,5,6,7,1,2,4,5,6,'Juan', 'Juan']
lista = set(lista) # Fazendo um cast da minha lista para criar um set, ele agora será um set e retira todos os valores duplicados
lista = list(lista) # Fazendo um cast de volta para lista, minha lista não terá mais valores duplicados.
print(lista)
print(lista[-1])

print('#'*40, '\n')
#########################################################################

#Verificação se as duas listas são mais iguais através de sets
l1 = ['Adilson', 'André', 'Tomaz', 'Lucas']
l2 = ['Adilson', 'André', 'André', 'André', 'Lucas','Lucas','Lucas', 'Tomaz', 'Tomaz',] 

#OBS: Sets não consideram valores duplicados - por isso as listas são iguais

if set(l1) == set(l2):
    print('L1 é igual a L2')
else:
    print('L1 é diferente de L2') 