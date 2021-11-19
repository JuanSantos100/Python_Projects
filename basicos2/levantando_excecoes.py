# def divide (n1, n2):
#     try:
#         return n1 / n2
#     except ZeroDivisionError as error:
#         print('Log: ', error)
#         raise #Faz o tratamento da exceção  e registro num log, raise faz com que a exceção seja enviada

# try:
#     print(divide(2, 0))
# except ZeroDivisionError as error:
#     print('Erro: ', error)

# print(divide(2,0))

print('#'* 40)


def divide2(n1, n2):
    if n2 == 0:
        raise ValueError('n2 não pode ser 0') # Levantando a minha própria exceção
    return n1/n2

try: 
    print(divide2(2,0))
except ValueError as error:
    print('Você está tentando dividir por 0')
    print(error)

