"""
Funções - def em Python (Parte 1)
"""

#Definicação de uma função

def funcao(msg): #Definicação de uma função que pode ou não receber parâmetros
    print(msg)



funcao('Olá mundo')
funcao('Olá mundo')
funcao('Olá mundo')
funcao('Olá mundo')
print('Hello World !!!')
print('Hello World !!!')
print('Hello World !!!')
print('Hello World !!!')

print('#' * 40)

##############################################
def saudacao(msg, nome):
    print(msg, nome)

mensagem = 'Olá tudo bem'
nome = 'Lucas Mateus'

saudacao(mensagem, nome)

print('#' * 40)

###############################################

#Assumindo valores padrão:

def mensagem(saudacao = 'Olá ', nome = 'usuário'): #Caso eu não queia solicitar valor ao usuário
    print(saudacao, nome)


mensagem()
mensagem(nome = 'Zezão')
mensagem(nome = 'Zezão', saudacao='Hi')
print('#' * 40)

###############################################

#Substituindo valores com replace()
def substituicao(saudacao = 'Olá ', nome = 'usuário'):
    nome = nome.replace('e', '3')
    saudacao = saudacao.replace('e', '3')
    print(saudacao, nome)

substituicao(nome='Zezinho', saudacao='Hello')

