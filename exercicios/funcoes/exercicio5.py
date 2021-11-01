"""
Crie uma função1 que recebe uma função2 como parâmetro e retorne
o valor da função2 executada
"""

def funcao1 (funcao):
    return funcao() # Retornando a execução da função

def funcao2():
    variavel2 = 'Esta variável foi criada na função 2'
    return variavel2

executando = funcao1(funcao2)
print(executando)


