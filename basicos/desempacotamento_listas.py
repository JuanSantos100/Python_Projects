"""
Desempacotamento de listas em python
"""

lista1 = ['Vitor', 'Mateus', 'André', 1,2,3,4,5,6,7,8,9,100]

n1, n2, n3, *lista_demais_itens, ultimo_valor = lista1 #Estou colocando o valor de cada índice da minha lista em uma variável
"""
Posso colocar a notação *lista_demais_itens para fazer uma lista com 
todos os demais valores da lista, sem a necessidade de escrever variáveis
para todos eles. 
"""

print(ultimo_valor)