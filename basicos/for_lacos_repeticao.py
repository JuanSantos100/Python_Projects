"""
For in em python
Iteração strings com for
Função range(start = 0, stop, setp=1)
"""

texto = 'Python'
novaString = ''
letra_usuario = ''
# ***USANDO WHILE***
# c = 0
# while c < len(texto):
#     print(texto[c])
#     c += 1

# ***USANDO FOR***
# for n, letra in enumerate(texto):
#     print(n, letra)

# for numero in range(100):
#     if numero % 8 == 0:
#         print(numero)


#Continue -> Pula para o próximo laço
#break -> Encerra o laço
for letra in texto: 
    if letra == 't':
        continue
        novaString = novaString + letra.upper()
    elif letra == 'h':
        novaString += letra.upper()
        break
    else:
        novaString += letra

print(novaString)