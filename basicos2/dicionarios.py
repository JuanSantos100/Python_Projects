"""
Dicionários {}

Estrutura de dados que suporta um par de chave e valor
"""

dicionario = {
    'chave1': 'valor da chave'
}

print(dicionario)

# Adicionando valores no dicionário
dicionario['nova_chave'] = 'Valor da nova chaves' 
print(dicionario)
print(dicionario['nova_chave'])

#Outra forma de criar lista
dicionario2 = dict(chave1 = 'Valor da chave', chave2 = 'Valor da outra chave')
print(dicionario2)

print('#' * 40)
#######################################################################

#Gerenciando listas

dicionario3 = { #Listas não podem ser usadas como CHAVE
    'chave1': 'Valor 1',
    'chave2': 'Valor 2',
    'chave3': 'Valor 3'
}

#Adicionando valores no dicionário
dicionario3['chave4'] = 'Valor 4'

if 'chave4' in dicionario3:
    print(dicionario3['chave4'])
# print('Oi')

# print(dicionario3.get('nomedachave')) Método para retornar o valor de uma chave em um dicionário. Se não existir a chave, apenas retorna None

dicionario3['chave5'] = 'Valor 5'
if dicionario3.get('chave5') is not None:
    print(dicionario3.get('chave5'))

print(dicionario3)

print('#' * 40, '\n')
#######################################################################

#Adicionando valores no dicionário
dicionario3.update({'chave6': 'Valor 6'})
print('Adicionado o par "chave6": {}'.format(dicionario3))

print('#' * 40, '\n')
#######################################################################

#Excluindo valores no dicionário
del dicionario3['chave1']
print('Após deletar "chave1": {}'.format(dicionario3))

dicionario3.pop('chave3')
print('Após deletar "chave3": {}'.format(dicionario3))

dicionario3.popitem()
print(print('Após deletar a última chave com popItem() : {}'.format(dicionario3)))

print('#' * 40, '\n')
#######################################################################

#Verificando se existe um valor no dicionário
print('Verificando se a chave: "chave2" está no dicionário: ', 'chave2' in dicionario3)
print('Verificando se um valor "Valor 2" existe na lista: ', 'Valor 2' in dicionario3.values())

print('#' * 40, '\n')
#######################################################################

# Verificando o tamanho do dicionário
print(len(dicionario3)) # O valor retornado será refenrete a quantidade de PARES no meu dicionário


print('#' * 40, '\n')
#######################################################################

#Iterando sobre dicionários

for chave, valor in dicionario3.items(): #dicionario3.keys() - retorna chaves | dicionario3.values() - retorna os valores | dicionario3.items() - retorna o par chave : valor
    print(chave, valor)


print('#' * 40, '\n')
#######################################################################

#Criando dicionários dentro de dicionários

clientes = {
    'cliente1': {
        'nome': 'Julia',
        'sobrenome': 'Miranda'
    }, 

    'cliente2': {
        'nome': 'Wagner',
        'sobrenome': 'Dieter'
    },

    'cliente3': {
        'nome': 'Maria',
        'sobrenome': 'Augusta'
    }
}

for cliente_chave, cliente_valor in clientes.items():
    print(f'Exibindo {cliente_chave}')
    for dados_chave, dados_valor in cliente_valor.items():
        print(f'\t {dados_chave} =  {dados_valor}') #\t dá um tab para justificar o texto


print('#' * 40, '\n')
#######################################################################

#Criando uma cópia no meu dicionário
"""
Apenas associar o meu dicionário a uma outra variável não irá funcionar
Ex.:

d = {1: 'Valor', 2: 'Valor 2'}
novo_dicionario = d


Para construir um novo dicionário a partir de um já existente
é necessário usar a função .copy()
"""

dictionary = {
    'chave1': 'valor1',
    'chave2': 'valor2'
}

novo_dictionary = dictionary.copy() #Criando uma cópia rasa do meu dicionário 

print(f'Dictionary: {dictionary}')
print(f'Novo_Dictionary: {novo_dictionary}')

novo_dictionary['chave2'] = 'valor_novo'
print(f'Novo_Dictionary: {novo_dictionary}')