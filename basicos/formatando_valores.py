"""
Formatação de valores
:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(NUMERO)f - Quantidade de casas deciamais :.2f
:(CARACTERE) (> OU < OU ^) (QUANTIDADE)(TIPO - s, d ou f)

> - Esquerda
< - Direta
^ - Centro

"""

nome = 'Juan Victor'
print(f'{nome:#^50}')

print('{:@>50}'.format(nome))

#print('{:$}'.format(nome))
num1 = 1
num2 = 1150

print(f'{num1:0>10}')

print(f'{num2:0<10}')

print(f'{num2:0^10}')

print(nome.upper())
print(nome.lower())
print(nome.title())

