lista = [
    ('chave', 'valores'),
    ('chave2', 'valor2')
]

d1 = {x for x in range(5)}
print(d1, type(d1))

print('#' * 40, '\n')
###################################################

d2 = {f'chave_{x}': x ** 2 for x in range(5)}
print(d2)