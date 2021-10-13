"""
Split , Join, Enumerate em Python

* Split - Dividir uma string # str
* Join - Juntar uma lista # str
* Emumerate - Enumerar elemnentos da lista # iteráveis
"""
string = 'O Brasil é o o o o o o país do futebol, o Brasil é penta.'
lista = string.split(' ') #Usando espeço para separar as palavras dentro de uma lista ('condição do split')
lista2 = string.split(',')


# Testes 1
for valor in lista:
    print(valor)


print('#'*20)

for valor in lista2:
    print(valor)

print('#'*20)

for valor in lista:
    print(f'A palavra {valor} apareceu {lista.count(valor)}x na frase.') #Faço uma contagem das vezes que um elemento apareceu.



# Testes 2
palavra = ''
contagem = 0
for valor in lista: #Fazendo a verificação de qual palavra apareceu mais vezes na frase
    qtdVezes = lista.count(valor)

    if qtdVezes > contagem:
        contagem = qtdVezes
        palavra = valor

print(f'A palavra que apareceu mais vezes é {palavra} ({contagem}x)')


# Teste 3
for valor in lista2:
    print(valor.strip().capitalize()) #.strip() faz com que os espaços do início e fim da string sejam removidos.
                                      #.capitalize faz com que os valores iniciais sejam maiúsculos


# Teste 4 --> JOIN 
string = 'O Brasil é penta'
lista = string.split(' ')
string2 = '-'.join(lista)

print(string)
print(lista)
print(string2)



# Teste 5 --> enumerate
string = 'O Brasil é penta.'
lista = string.split(' ')

for indice, valor_lista in enumerate(lista):
    print(indice, valor_lista, lista[indice])


# Teste 6
lista = [
    [0,'Lista'],
    [1,'João'],
    [2,'Maria']
]

for indice, nome in enumerate(lista):
    print(indice, nome)

# print(lista)
# print(lista2)
