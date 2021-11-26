import pacote_1_vendas.calculos
from pacote_1_vendas import calculos
from pacote_1_vendas.formata.preco import converteReal as converteReal

preco_produto = 49.90
preco_com_aumento = calculos.aumento(preco_produto, 15, formata=True)
print(preco_com_aumento)

preco_com_reducao = calculos.reducao(preco_produto, 15, formata=True)
print(preco_com_reducao)

print(converteReal(54.84))