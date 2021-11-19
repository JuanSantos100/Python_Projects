"""
Usando módulos em python
"""

# import sys



#Ou importando somente algumas funções do módulo
from sys import platform as sistema_operacional
print(sistema_operacional)

print('#' * 40, '\n')

print('Módulo random')

from random import randint
for valor in range(0, 10):
    print(randint(0,10))