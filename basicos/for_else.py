"""
For / Else em Python
"""

strings = ['Juan Victor', 'André', 'Lucas']
# for valor in strings:
#     print(valor)
#     # continue
#     break
#     print(valor)

# for valor in strings:
#     if valor.startswith('J'):
#         print('Essa letra começa com J || Palavra: ', valor)
#     else:
#         print('Essa letra não começa com J || Palavra: ', valor)

for valor in strings:
    print(valor)
    if valor.lower().startswith('j'):
        break
else: 
    print('Não existe uma palavra que começa com J')