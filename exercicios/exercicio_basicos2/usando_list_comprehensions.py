"""

string = '01234567890123456789012345678901234567890123456789'
Separar a string em vários grupos: 
"""

string = '0123456789012345678901234567890123456789012345678901234567890123456789'
step = 10
grupo_lista = [string[i:i+step] for i in range(0, len(string), step)]
print(grupo_lista)

retorno = '.'.join(grupo_lista)
print(retorno)