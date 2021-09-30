"""
Comentários para maior quantidade de linhas
"""

"""
Comandos prints
"""
print('Hello World')


#sep='' irá separar os itens do print de acordo com o que for inserido
#end='' acrescenta o caractere ao final do meu conteúdo do print()
print('824', '176', '070', sep='.', end='-') 
print('Esse é o meu \'texto\' (str)')
print(r'this is my \n text')  #r permite que nenhum código seja executado entre ''



"""
Tipos primitivos
"""

print('Luiz', type('Luiz')) #String
print(10, type(10)) #int
print(25.23, type(25.23)) #float
print('l' == 'L', type('l' == 'L')) #boolean


"""
Operadores Aritiméticos
"""

"""
+ soma, 
- subtração, 
multiplicação *, 
divisão /,
exponenciação **,
divisão para sobrar inteiro //, 
resto da divisão%, 
()
"""
 
print('Resto da divisao', 10 % 2)

"""
Variáveis

"""


nome = 'Luiz Otávio'
idade = 32
altura = 1.80
e_maior = idade > 18
data_1 = True
data_atual = 2019
peso = 80
print('Nome: ', nome)
print('idade: ', altura)
print('Idade x altura: ', idade * altura)

imc = peso / (altura ** 2)

print('O IMC do ', nome, ', com a idade ', idade, ' é igual à: ', imc )