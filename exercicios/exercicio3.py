"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 lettras
ou menos, escreva: "seu nome é pequeno"; se o nome tiver entre 5 e 6 letras, escreva
"seu nome é normal". Se o nome for maior que 6 letras escreva: "Seu nome é muito grande"
"""

nome = input('Digite seu nome: ')
tamanho = len(nome)  #len() devolve o tamanho da string


if tamanho <= 4:
    print('Seu nome é pequeno')
elif tamanho <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')
