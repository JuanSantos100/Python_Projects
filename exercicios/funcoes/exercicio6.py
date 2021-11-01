"""
Crie uma função1 que recebe uma função2 como parâmetro e retorne
o valor da função2 executada. Faça a função 1 executar duas funções que
recebam um número diferentes de argumentos
"""

def funcao_mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)

def fala_oi (nome):
    return f'Oi {nome}'

def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'

executando = funcao_mestre(fala_oi, 'Julia')
executando2 = funcao_mestre(saudacao, 'Luiz', saudacao='Bom dia !')
print(executando)
print(executando2)
    