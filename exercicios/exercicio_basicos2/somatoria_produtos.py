"""
Somatória de produtos em um sistema  de carrinho - USANDO LIST COMPREHENSIONS
"""


carrinho = []

carrinho.append(('Produto 1', 20 ))
carrinho.append(('Produto 2', 10 ))
carrinho.append(('Produto 3', 60 ))
carrinho.append(('Produto 4', 100 ))
carrinho.append(('Produto 5', 78 ))
carrinho.append(('Produto 6', 70 ))
carrinho.append(('Produto 7', 60 ))
carrinho.append(('Produto 8', 80 ))
carrinho.append(('Produto 9', 90 ))
carrinho.append(('Produto 10', 40 ))
# Resultado = 608

#Solução 1
# total = 0
# for valor in carrinho:
#     total += valor[1]
# print(total)

#Solução 2
# total = []
# for valor in carrinho:
#     total.append(valor[1])

# print(sum(total))

total_carrinho = sum([total[1] for total in carrinho])
print(f'Total: R${total_carrinho}')