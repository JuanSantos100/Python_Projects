"""
Índices de Strings
Fatiamento Strings [inicio:fim:passo]
quando eu declaro um indice, o fatiamento vai até (declaracao - 1)
"""

#positivos      [012345678]
texto =         'Python s2'
#negativos     -[987654321]

novaString = texto[2:6] #Início : Fim
print(novaString)
novaString2 = texto[:6] #do início até a minha declaração
print(novaString2)
novaString3 = texto[5:] #da minha declaração até o fim 
print(novaString3)
novaString4 = texto[:9:2]
print(novaString4)