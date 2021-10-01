"""
* Criar variáveis para nome, idade, altura
* e peso de uma pessoa
* Criar variável com o ano atual
* Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
* Obter o IMC da pessoa com 2 casas decimais (peso e altura da pessoa)
Exibir um texto com otodos os valores na tela usando F-Strings (com chaves)
"""

nome = 'Juan Victor'
idade = 20 
altura = 1.95
peso = 98.0
anoAtual = 2021

dataNascimento = anoAtual - idade
imc = peso / altura ** 2

print('{} tem {} anos, {} de altura e pesa {}kg'.format(nome, idade, altura, peso))
print('O IMC de {} é {:.2f}'.format(nome, imc))
print('{} nasceu em {}.'.format(nome, dataNascimento))

#Outra forma de fazer usando print(f'')
print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}kg')
print(f'O IMC de {nome} é {imc:.2f}')
print(f'{nome} nasceu em {dataNascimento}')

