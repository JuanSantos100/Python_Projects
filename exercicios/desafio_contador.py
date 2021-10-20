"""
Criar um contador que vá de 0 a 8 e 10 a 2 
ao mesmo tempo
"""

#Solução possível
lista = [10,9,8,7,6,5,4,3,2]

for c1, c2 in enumerate(lista):
    print(c1, c2)


#Solução do curso
for i, r in enumerate(range(10, 1, -1)):
    print(i, r)
