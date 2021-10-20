"""
Operador Ternário em python
"""
# Exemplo sem usar operadores
# logged_user = False

# if logged_user:
#     msg = 'Usuário logado!'
# else:
#     msg = 'Usuário precisar logar'

# print(msg)

# Exemplo com operadores
logged_user = True
msg = 'Usuário logado' if logged_user else 'Usuário precisa logar'
print(msg)


# idade = 18
# if idade >= 18:
#     print('Pode acessar')
# else:
#     print('não pode acessar')

idade = input('Digite a sua idade: ')
if not idade.isnumeric():
    print('você precisa digitar apenas números')
else:
    idade = int(idade)
    e_de_maior = (idade >=18)
    msg = 'Pode acessar' if e_de_maior else 'Não pode acessar'
    print(msg)

