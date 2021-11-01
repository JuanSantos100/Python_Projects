"""
Crie uma função que recebe 2 números. O primeiro é um valor eo segundo 
um percentual. Retorne (return) o valor do primeiro número somado
do aumento do percentual do mesmo.
"""

def soma_percentual(valor, porcentual):
    porcento = porcentual / 100
    resultado = valor + (valor * porcento)
    return resultado

valor = int(input('Digite um número: '))
porcentual = int(input('Digite um valor para calcular a porcentagem: '))

resultado = int(soma_percentual(valor, porcentual))
print(resultado)

